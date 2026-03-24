import functools
from flask import (
    Blueprint, flash,g, redirect, render_template, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# importing the forms
from VibeSync.forms import RegistrationForm, LoginForm
# importing the database
from VibeSync.extensions import db
from VibeSync.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET','POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.query.filter_by(username=username).first() is not None:
            error = 'User {} is already registered.'.format(username)
        
        if error is None:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html',form=form)



@bp.route('/login', methods=('GET','POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('blog.index')) 

        flash(error)

    return render_template('auth/login.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None: 
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
