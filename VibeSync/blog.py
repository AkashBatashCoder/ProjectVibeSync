from flask import (
    Blueprint, flash, redirect, render_template, url_for    
)
from werkzeug.exceptions import abort
from VibeSync.forms import PostForm, UpdatePostForm, DeletePostForm
from VibeSync.extensions import db
from VibeSync.models import Post
from sqlalchemy.orm import selectinload
from flask_login import login_required, current_user

bp = Blueprint('blog', __name__)


@bp.route('/feed')
@login_required
def index():
    posts = Post.query.options(selectinload(Post.author)).order_by(Post.created.desc()).all()   
    return render_template('blog/index.html', posts=posts)



@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        error = None

        if not title:
            error = 'Title is required.'

        if error is None:
            new_post = Post(title=title, body=body, author_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('blog.index'))
        
        flash(error)

    return render_template('blog/create.html',form=form)



def get_post(id, check_author=True):
    post = Post.query.get_or_404(id)
    if check_author and post.author_id != current_user.id:
        abort(403)
    return post   


@bp.route('/<int:id>/update', methods=('GET','POST'))
@login_required
def update(id):
    post = get_post(id)
    form = UpdatePostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('blog.index'))


    return render_template('blog/update.html', post=post, form=form)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    form = DeletePostForm()
    if form.validate_on_submit():
        post = Post.query.get(id)
        if post is None:
            abort(404, f"Post id {id} doesn't exist.")
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('blog.index'))