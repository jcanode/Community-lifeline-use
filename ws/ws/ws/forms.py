from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(Form):
    """Login form to access writing and settings pages"""
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class RegisterForm(Form):
    """Registration form to create an account"""
    email = StringField('email', validators=[DataRequired()])
    password1 = PasswordField('password1', validators=[DataRequired()])
    password2 = PasswordField('password2', validators=[DataRequired(),EqualTo('password1', message='Passwords must match')])