import functools
from flask import (
    Blueprint, flash, redirect, render_template, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# importing the forms
from VibeSync.forms import RegistrationForm, LoginForm
# importing the database
from VibeSync.extensions import db
from VibeSync.models import User
from flask_login import login_user, logout_user
from .extensions import login_manager


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
            login_user(user,remember=True) # form.remember.data is used for chackbox
            return redirect(url_for('blog.index')) 

        flash(error)

    return render_template('auth/login.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    '''Flask-Login user loader callback. This function is used to reload the user object from the user ID stored in the session.
    This function is used by Flask-Login to load the user from the database when the user is logged in. It takes the user_id as an argument and returns the corresponding User
    '''
    return User.query.get(int(user_id))



@bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('blog.index'))


