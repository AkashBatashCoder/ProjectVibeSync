from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Create Post')

class UpdatePostForm(FlaskForm):
    # Will update later / need to load the existing post data first
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update Post')

class DeletePostForm(FlaskForm):
    submit = SubmitField('Delete Post')

