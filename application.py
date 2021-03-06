import os
from time import localtime, strftime
from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from wtform_fields import *
from models import *

app = Flask(__name__)
# actual secret key if running on a local system => "b'0\x17\xdb\x03\xdc\x0c;ja\xecv\xb0a\xe9$\x13'"
app.secret_key = app.secret_key = os.environ.get("SECRET")


# configure database
# Actual Database url if running on a local system => "postgres://xwawslekazwoni:ba0ee8e746269e7cc8ff5804aa28c3205e0309757bb2673ffad22d793bb13b92@ec2-34-225-162-157.compute-1.amazonaws.com:5432/dcqg3bakntjhp"
app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

# Initialize Flask-SocketIO
socketio = SocketIO(app)
ROOMS = ["Main", "General", "games", "coding"]

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

        flash('Registered Successfully, Please Login.', 'success')
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
        flash('PLEASE LOGIN', 'danger')
        return redirect(url_for('login'))

    return render_template('chat.html', username=current_user.username, rooms=ROOMS)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


# event buckets
@socketio.on('incoming-msg')
def on_message(data):
    """Broadcast messages"""

    msg = data["msg"]
    username = data["username"]
    room = data["room"]
    # Set timestamp
    time_stamp = strftime('%b-%d %I:%M%p', localtime())
    send({"username": username, "msg": msg, "time_stamp": time_stamp}, room=room)


# Join the room
@socketio.on('join')
def join(data):
    join_room(data['room'])
    send({'msg': data['username'] + " is online in " +
                 data['room'] + " room."}, room=data['room'])


# Leave the room
@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send({'msg': data['username'] + " is offline of  " +
                 data['room'] + " room."}, room=data['room'])


if __name__ == "__main__":
    # remove the code below and use "socketio.run(app, debug=True)" if running on a local system
    app.run()
