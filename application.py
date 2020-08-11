from flask import Flask, render_template

from wtform_fields import *
from models import *

app = Flask(__name__)
app.secret_key = 'replace later'

#configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://xwawslekazwoni:ba0ee8e746269e7cc8ff5804aa28c3205e0309757bb2673ffad22d793bb13b92@ec2-34-225-162-157.compute-1.amazonaws.com:5432/dcqg3bakntjhp'

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()

    """trigger validators"""
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "inserted in the database"

    """returns rendered html pages in that route"""
    return render_template("index.html", form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)

