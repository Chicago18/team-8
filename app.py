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
    

@app.route("/ParentPortal")
def test3():
	return render_template("/concept-clean/index.html")


@app.route("/Enrollment")
def Enrollment():
	return "Form1: "