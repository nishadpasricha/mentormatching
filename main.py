from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/studentsubmit',methods= ['GET', 'POST'])
def studentsubmit():
    return render_template('studentsubmit.html')


@app.route('/studentform', methods = ['GET','POST'])
def studentform():
    return render_template('studentform.html')


#testing staging