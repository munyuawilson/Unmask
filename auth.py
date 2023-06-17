
from flask import request,render_template,flash,session,redirect
from flask_login import login_user, logout_user, current_user, login_required
from model import Users,db
from main import app


@app.route('/login',methods=['POST',"GET"])
def login():
    
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        

        query=Users.query.filter_by(email=email).first()
        print(query)
        if query!=None:
            if query.password==password:
                session["username"]=query.name
                user = Users.query.get(query.id)
                login_user(user)
                session["email"]=query.email
                

                return redirect('/dashboard')
            else:
                flash("Wrong Email or Password!")
                
        else:
            flash("No search user!")
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
            flash("User already there!")
        else:
            
            new_user=Users(name=name, number=number,email=email,password=password,credits=30)
            db.session.add(new_user)
            db.session.commit()
                
                
            flash("Account created!")


    return render_template("signup.html")


