from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("test.html")


@app.route("/assignments")
def test():
    return "assignments page"


@app.route("/character")
def test2():
    return "characters page"
    

@app.route("/ParentsPortal")
def test3():
	return "Hello, [Parent]! Welcome to [Child]'s report"
