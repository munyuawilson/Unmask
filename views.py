from flask import request,render_template,redirect

from model import *
from main import *


with app.app_context():
    db.create_all()

@app.route("/add",methods=["POST","GET"])

def add():
    if request.method == "POST":
        
        name = request.form.get('name')
        number = request.form.get('number')
        email = request.form.get('email')
        social_media = request.form.get('socials')
        reason = request.form.get('reason')

        new_con=Conmen(name=name,number=number,email=email,social_media=social_media,reason=reason)
        db.session.add(new_con)
        db.session.commit()

        
        #add images for proof
        #images can be stored in compressed folders

        #add this to database

        #save to database
    return render_template('add.html')
@app.route('/search',methods = ['POST',"GET"])
def search():
    number=request.form.get('number')


    number=Conmen.query.filter_by(number=number).first()
    print(number.email)

    return number.email
@app.route('/pay', methods = ["POST","GET"])
def pay():
    #payment for the search
    pass
@app.route('/logout',methods=["POST","GET"])
def logout():
    pass

