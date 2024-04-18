from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin



db=SQLAlchemy()

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    number=db.Column(db.Integer)
    email=db.Column(db.String(100))
    password=db.Column(db.String(120))
    credits=db.Column(db.Integer)

    def __init__(self,name,number,email,password,credits,is_active=True):
        
        self.name=name 
        
        self.number=number
        self.email=email
        self.password=password
        self.credits=credits
        self.is_active = is_active

    def is_active(self):
        return self._is_active
    
class Conmen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    number = db.Column(db.Integer)
    email = db.Column(db.String(120))
    social_media = db.Column(db.String(120))
    reason = db.Column(db.String(120))
    image=db.Column(db.LargeBinary)
    def __init__(self,name,number,email,social_media,reason,image):
        
        self.name=name 
        
        self.number=number
        self.email=email
        self.social_media=social_media
        self.reason=reason
        self.image=image