from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')