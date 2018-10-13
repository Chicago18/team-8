from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/assignments")
def test():
    return "assignments page"


@app.route("character")
def test2():
    return "characters page"
