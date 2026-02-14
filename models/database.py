from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # investor / owner

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)

    loan_amount = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    revenue = db.Column(db.Float)
    cost = db.Column(db.Float)

    delay = db.Column(db.Integer)
    inflation = db.Column(db.Float)
    revenue_drop = db.Column(db.Float)

    risk = db.Column(db.String(50))
    probability = db.Column(db.Integer)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
