from flask import Flask
from flask import render_template
app = Flask(__name__)

user = {'userName': 'Rohit', 
		'childName': 'Megha'}

child = {'childName': 'Megha',
		 'grade': 4,
		 'englishGrade': "D",
		 'mathGrade': "E",
		 'scienceGrade': "C"}

@app.route("/")
def hello():
    return render_template("test.html")


@app.route("/assignments")
def test():
    return "assignments page"


@app.route("/character")
def test2():
    return "characters page"

@app.route("/Home")
def home():
	return render_template("/concept-clean/index.html")    

@app.route("/ParentPortal")
def test3():
	return render_template("/concept-clean/ParentPortal.html", user=user)


@app.route("/Enrollment")
def Enrollment():
	return render_template("/concept-clean/form.html", user=user, child=child)