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

@app.route("/Student")
def student():
	return render_template("/concept-clean/fullwidth.html") 

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

@app.route("/Report_Card")
def report():
	return render_template("concept-clean/index_k.html")

@app.route("/junior")
def report1():
	return render_template("concept-clean/table20182019.html")

@app.route("/soph")
def report2():
	return render_template("concept-clean/table20172018.html")

@app.route("/fresh")
def repor3():
	return render_template("concept-clean/table20162017.html")

@app.route("/Attendance")
def attend():
	return render_template("concept-clean/attendance.html")

@app.route("/Assignments")
def assignments():
	return render_template("concept-clean/assignments.html")