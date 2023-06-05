from flask_sqlalchemy import SQLAlchemy



db=SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    number=db.Column(db.Integer)
    email=db.Column(db.String(100))
    password=db.Column(db.String(120))
    def __init__(self,name,number,email,password):
        
        self.name=name 
        
        self.number=number
        self.email=email
        self.password=password

class Conmen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    number = db.Column(db.Integer)
    email = db.Column(db.String(120))
    social_media = db.Column(db.String(120))
    reason = db.Column(db.String(120))
    image=db.Column(db.LargeBinary)
    def __init__(self,name,number,email,password):
        
        self.name=name 
        
        self.number=number
        self.email=email
        self.password=password


    

