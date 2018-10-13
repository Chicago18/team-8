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

@app.route("/Enrollment/Form1")
def Form1():
	return render_template("/concept-clean/form1.html", user=user, child=child)

@app.route("/Enrollment/Form2")
def Form2():
	return render_template("/concept-clean/form2.html", user=user, child=child)

@app.route("/Enrollment/Form3")
def Form3():
	return render_template("/concept-clean/form3.html", user=user, child=child)

@app.route("/Enrollment/Form4")
def Form4():
	return render_template("/concept-clean/form4.html", user=user, child=child)