from flask import Flask
from flask_login import  LoginManager



app=Flask(__name__,static_url_path="/static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Unmask.db'
app.secret_key = 'unmask'
from model import db,Users
db.init_app(app)
from views import *
from auth import *


from main import app
login=LoginManager()
login.init_app(app)

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

if __name__=="__main__":
    app.run(debug=True)