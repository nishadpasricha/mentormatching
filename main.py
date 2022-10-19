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
        student_email=request.form
        email=request.form.get("email")
        print(email)
    return render_template('studentform.html', user_info=student_email, email = email)