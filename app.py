from crypt import methods
from re import L
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#add DB 

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' <-- Local DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bcglbxjgveomly:fe71e32c012342bcb9dee8b2b7691f36d473414981bc80cfbe2d8feaf722ad8c@ec2-54-165-184-219.compute-1.amazonaws.com:5432/dcn9njuu2v97e7'


app.config['SECRET_KEY'] = "my secret key"

#InitDB

db = SQLAlchemy(app)

#Create a Model
class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),nullable=False)
    lname = db.Column(db.String(200),nullable=False)
    fname = db.Column(db.String(200),nullable=False)
    degree = db.Column(db.String(200),nullable=False)
    hobby1 = db.Column(db.String(200),nullable=False)
    hobby2 = db.Column(db.String(200),nullable=False)
    workexp = db.Column(db.String(200),nullable=False)
    dept = db.Column(db.String(200),nullable=False)
    interest = db.Column(db.String(200),nullable=False)
    desire = db.Column(db.String(200),nullable=False)
    graddate = db.Column(db.Integer)
    location = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    #Create a string

    def __repr__(self):
        return '<Name %r>' % self.name

#Alumni Table        
class Alumni(db.Model):
    __tablename__ = 'alumni'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),nullable=False)
    lname = db.Column(db.String(200),nullable=False)
    fname = db.Column(db.String(200),nullable=False)
    degree = db.Column(db.String(200),nullable=False)
    hobby1 = db.Column(db.String(200),nullable=False)
    hobby2 = db.Column(db.String(200),nullable=False)
    workexp = db.Column(db.String(200),nullable=False)
    dept = db.Column(db.String(200),nullable=False)
    graddate = db.Column(db.Integer)
    location = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name

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
        global s_email
        s_email = request.form.get("email")
        print(s_email)
    return render_template('studentform.html')

@app.route('/studentconfirm', methods = ['GET','POST'])
def studentconfirm():
    if request.method == 'POST':
        global s_fname,s_lname,s_degree,s_hobby1,s_hobby2,s_workexp,s_dept,s_interest,s_desire,s_graddate,s_location,s_linkedin
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
        student = Students(email=s_email, lname=s_lname,fname=s_fname,degree=s_degree,hobby1=s_hobby1,hobby2=s_hobby2,workexp=s_workexp,dept=s_dept,interest=s_interest,desire=s_desire,graddate = s_graddate, location=s_location,linkedin=s_linkedin)

        db.session.add(student)
        db.session.commit()
        

        print(s_email, s_lname, s_fname,s_degree,s_hobby1,s_hobby2,s_workexp,s_dept,s_interest,s_desire,s_graddate,s_location,s_linkedin)
    return render_template('studentconfirm.html', s_fname = s_fname)

@app.route('/alumniemailcheck', methods = ['GET','POST'])
def alumniemailcheck():
    return render_template('alumniemailcheck.html')

@app.route('/alumniform', methods = ['GET','POST'])
def alumniform():
    if request.method == 'POST':
        request.form
        
        session['a_email'] = request.form.get("email")
        
    return render_template('alumniform.html')

@app.route('/alumniconfirm', methods = ['GET','POST'])
def alumniconfirm():
    if request.method == 'POST':
        request.form
        global a_fname,a_lname,a_degree,a_hobby1,a_hobby2, a_workexp, a_dept, a_graddate, a_location,a_linkedin
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
        a_email = session.get('a_email',None)
        alumni = Alumni(email=a_email,fname=a_fname,lname=a_lname,degree=a_degree,hobby1=a_hobby1,hobby2=a_hobby2,workexp=a_workexp,dept=a_dept,graddate=a_graddate,location=a_location,linkedin=a_linkedin)
        db.session.add(alumni)
        db.session.commit()
        print( a_fname, a_lname, a_degree, a_hobby1,a_hobby2,a_workexp, a_dept,a_graddate, a_location,a_linkedin)
    return render_template('alumniconfirm.html', a_fname = a_fname)

