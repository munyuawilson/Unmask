from flask import Flask



app=Flask(__name__,static_url_path="/static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Unmask.db'
app.secret_key = 'unmask'
from model import db
db.init_app(app)
from views import *
from auth import *


from main import app


if __name__=="__main__":
    app.run(debug=True)