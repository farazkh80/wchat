from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from wtform_fields import *
from models import *

app = Flask(__name__)
app.secret_key = 'replace later'

# configure database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://xwawslekazwoni:ba0ee8e746269e7cc8ff5804aa28c3205e0309757bb2673ffad22d793bb13b92@ec2-34-225-162-157.compute-1.amazonaws.com:5432/dcqg3bakntjhp'

db = SQLAlchemy(app)

# configure flask login
login = LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(id):

    return User.query.get(int(id))


@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()

    """trigger validators and update database if the validation was successful"""
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # hashing the password
        hashed_passwd = pbkdf2_sha256.hash(password)

        user = User(username=username, password=hashed_passwd)
        db.session.add(user)
        db.session.commit()

        # redirect the user to the login route
        return redirect(url_for('login'))

    """returns rendered html pages in that route"""
    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Allow login if validation successful
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))



    return render_template("login.html", form=login_form)

@app.route("/chat", methods=['GET', 'POST'])
def chat():
    if not current_user.is_authenticated:
        return "Please Login for accessing this Page!"
    return "WELCOME!"

@app.route('/logout', methods=['GET'])
def logout():

    logout_user()
    return "logged out using flask_login"


if __name__ == "__main__":
    app.run(debug=True)
