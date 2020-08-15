from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from passlib.hash import pbkdf2_sha256
from models import User


def invalid_credentials(form, field):
    username_entered = form.username.data
    password_entered = field.data

    # check the username
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or Password is incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username or Password is incorrect")


class RegistrationForm(FlaskForm):
    """ Registration Form Parameters and Validators"""
    username = StringField('username_label',
                           validators=[InputRequired(message="Username Required"),
                                       Length(min=4, max=25, message="Username must be between 4 and 25 characters")])

    password = PasswordField('password_label',
                             validators=[InputRequired(message="Password Required"),
                                         Length(min=4, max=25, message="Password must be between 4 and 25 characters")])
    confirm_password = PasswordField('confirm_password_label',
                                     validators=[InputRequired(message="Password Required"),
                                                 EqualTo('password', message="Passwords must match")])

    # checks if the user exists
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists, Please choose another one.")


class LoginForm(FlaskForm):
    """Login form"""

    username = StringField('username_label',
                           validators=[InputRequired(message="Username Required")])
    password = PasswordField('password_label',
                             validators=[InputRequired(message="Password Required"), invalid_credentials])