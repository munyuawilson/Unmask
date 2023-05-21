from flask_sqlalchemy import SQLAlchemy
from main import app

db=SQLAlchemy(app)

class Conmen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    number = db.Column(db.Integer)
    email = db.Column(db.String(120))
    social_media = db.Column(db.String(120))
    reason = db.Column(db.String(120))
    

