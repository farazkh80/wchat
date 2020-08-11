from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import *


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
    submit_button = SubmitField('Submit')

    # checks if the user exists
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists, Please choose another one.")
