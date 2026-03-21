from types import SimpleNamespace

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session       
)
from werkzeug.exceptions import abort
from VibeSync.auth import login_required
from VibeSync.db import get_db
from VibeSync.forms import PostForm, UpdatePostForm, DeletePostForm

bp = Blueprint('blog', __name__)


@bp.route('/feed')
@login_required
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
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
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('blog/create.html',form=form)



def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET','POST'))
@login_required
def update(id):
    post = get_post(id)
    post_obj = SimpleNamespace(**post)
    form = UpdatePostForm(obj=post_obj)
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        db = get_db()
        db.execute(
            'UPDATE post SET title = ?, body = ? WHERE id = ?',
            (title, body, id)
        )
        db.commit()
        return redirect(url_for('blog.index'))


    return render_template('blog/update.html', post=post, form=form)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    form = DeletePostForm()
    if form.validate_on_submit():
        get_post(id)
        db = get_db()
        db.execute('DELETE FROM post WHERE id = ?', (id,))
        db.commit()
    return redirect(url_for('blog.index'))