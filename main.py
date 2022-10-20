from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory



app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/studentsubmit',methods= ['GET', 'POST'])
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