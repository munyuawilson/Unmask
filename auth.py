
from flask import request,render_template,flash,session,redirect
from model import Users,db
from main import app


@app.route('/login',methods=['POST',"GET"])
def login():
    
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        

        query=Users.query.filter_by(email=email).first()
        if query:
            if query.password==password:
                session["username"]=query.name
                print("graeat")

                return redirect('/dashboard')
        else:
            print("Wrong Email or Password!")
    return render_template("login.html")
@app.route('/signin',methods=['POST',"GET"])
def signin():
    if request.method=="POST":
        with app.app_context():
            db.create_all()
        name=request.form.get("name")
        email=request.form.get("email")
        number=request.form.get("number")
        password=request.form.get("password")
        query=Users.query.filter_by(email=email).first()

        if query:
            print("User already there!")
        else:
            new_user=Users(name=name, number=number,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            print("recorded")
            redirect("/dashboard")


    return render_template("signup.html")


