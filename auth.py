from main import *
from flask import request,render_template,flash,session,redirect
from model import *



@app.route('/login',methods=['POST',"GET"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        db.engine.exec

        query=Users.query.filter_by(email=email).first()
        if query:
            if query.password==password:
                session["username"]=query.name
                print("graeat")

                redirect('/dashboard')
        else:
            flash("Wrong Email or Password!")
    return render_template("login.html")
@app.route('/signin',methods=['POST',"GET"])
def signin():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        number=request.form.get("number")
        password=request.form.get("password")
        query=Users.query.filter_by(email=email).first()

        if query:
            flash("User already there!")
        else:
            new_user=Users(name=name, number=number,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            redirect("/dashboard")

    return render_template("signup.html")


