from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """ Registration Form
    """
    username = StringField('username_label')
    password = PasswordField('password_field')
    confirm_password = PasswordField('confirm_password_label')
