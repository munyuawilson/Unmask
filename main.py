from flask import Flask
app=Flask(__name__,static_url_path="/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Unmask.db'
from views import *

from model import *

with app.app_context():
    db.create_all()
from auth import *
if __name__=="__main__":
    app.run(debug=True)