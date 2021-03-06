from flask.sqlalchemy import SQLAchemy
import datetime

db = SQLAchemy()

class User(db.Model):
    __table__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(66))
    created_date = db.Column(db.DateTime, default = datetime.datetime.now) 