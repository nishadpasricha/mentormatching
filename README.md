# mentormatching
MGIS 550


to run env in cd to MentorMatching folder:

export FLASK_APP=main.py
export FLASK_ENV=development
flask run



To edit DB instance, edit model in app.py

Then to push:

in terminal:

cd mentormatching

python

from app import app 
from app import db
from flask import current_app

with app.app_context():
  db.create_all()
 
