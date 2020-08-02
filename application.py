from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'replace later'


@app.route("/", methods=['GET', 'POST'])
def index():
    """reg_form = RegistrationForm()"""
    """returns rendered html pages in that route"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
