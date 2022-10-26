from crypt import methods
from re import L
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from datetime import datetime


app = Flask(__name__)
#add DB

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/studentemailcheck',methods= ['GET', 'POST'])
def studentsubmit():
    return render_template('studentemailcheck.html')


@app.route('/studentform', methods = ['GET','POST'])
def studentform():
    if request.method == 'POST':
        request.form
        email = request.form.get("email")
        print(email)
    return render_template('studentform.html')

@app.route('/studentconfirm', methods = ['GET','POST'])
def studentconfirm():
    if request.method == 'POST':
        request.form
        s_fname = request.form.get("fname")
        s_lname = request.form.get("lname")
        s_degree = request.form.get("degree")
        s_hobby1 = request.form.get("hobbies1")
        s_hobby2 = request.form.get("hobbies2")
        s_workexp = request.form.get("we")
        s_dept = request.form.get("s-department")
        s_interest = request.form.get("s-interest")
        s_desire = request.form.get("desire")
        s_graddate = request.form.get("graddate")
        s_location = request.form.get("location")
        s_linkedin = request.form.get("linkedin")

        print(s_lname, s_fname,s_degree,s_hobby1,s_hobby2,s_workexp,s_dept,s_interest,s_desire,s_graddate,s_location,s_linkedin)
    return render_template('studentconfirm.html', s_fname = s_fname)

@app.route('/alumniemailcheck', methods = ['GET','POST'])
def alumniemailcheck():
    return render_template('alumniemailcheck.html')

@app.route('/alumniform', methods = ['GET','POST'])
def alumniform():
    if request.method == 'POST':
        request.form
        email = request.form.get("email")
        print(email)
    return render_template('alumniform.html')

@app.route('/alumniconfirm', methods = ['GET','POST'])
def alumniconfirm():
    if request.method == 'POST':
        request.form
        a_fname = request.form.get("fname")
        a_lname = request.form.get("lname")
        a_degree = request.form.get("degree")
        a_hobby1 = request.form.get("hobbies1")
        a_hobby2 = request.form.get("hobbies2")
        a_workexp = request.form.get("we")
        a_dept = request.form.get("a-department")
        a_graddate = request.form.get("graddate")
        a_location = request.form.get("location")
        a_linkedin = request.form.get("linkedin")
        print(a_fname, a_lname, a_degree, a_hobby1,a_hobby2,a_workexp, a_dept,a_graddate, a_location,a_linkedin)

    return render_template('alumniconfirm.html')

