from flask import request,render_template,redirect,session,flash
from flask_login import login_user, logout_user, current_user, login_required
from model import Users,db,Conmen
from main import app
from sendemail import sendEmail
from flask_migrate import Migrate
import base64
import imghdr
from intasend import APIService


with app.app_context():
    db.create_all()

@app.route("/add",methods=["POST","GET"])
@login_required

def add():
    if request.method == "POST":
        
        name = request.form.get('name')
        number = request.form.get('number')
        email = request.form.get('email')
        social_media = request.form.get('socials')
        reason = request.form.get('reason')
        image=request.files['image']
        search_query=Conmen.query.filter_by(number=number).first()
        if search_query:
            flash("User already there!")
        else:
            new_con=Conmen(name=name,number=number,email=email,social_media=social_media,reason=reason, image=image.read())
            db.session.add(new_con)
            db.session.commit()

    email=session['email'] 
    username=session['username'] 
    credits=Users.query.filter_by(email=email).first().credits
    
        
    return render_template('addd.html',username=username,credits=credits)

@app.route('/search',methods = ['POST',"GET"])
@login_required
def search():
    username=session['username']
    email=session['email'] 
    credits=Users.query.filter_by(email=email).first().credits
    if request.method=="POST":
        search=request.form.get("search")
        search_query=Conmen.query.filter_by(number=search).first()
        if credits==0 or None:
            flash("No credits")
            
        elif credits==None:
            flash("No credits")    
        else:
            if search:
             if search_query:
                image=search_query.image
                image = base64.b64encode(image).decode('utf-8')

                credits=credits-10
                
                query=Users.query.filter_by(email=email).first()
                query.credits=credits
            
                db.session.commit()
        
        
            

                return render_template("searchh.html", search_result=search_query,username=username,image=image,credits=credits)
        
            else:
                flash("No search result")
                
     

    return render_template("searchh.html",username=username,credits=credits)

@app.route('/logout',methods=["POST","GET"])
def logout():
    logout_user()
    return redirect("/")

@app.route('/', methods = ["POST","GET"])
def home():
    if request.method=='POST':
        #write a script to send email
        
        name=request.form.get('name')
        sender_email=request.form.get('email')
        message=request.form.get('message')
        sendEmail(name,sender_email,message)
        
        

    return render_template("main.html")
    
@app.route('/dashboard', methods = ["POST","GET"])
@login_required
def dashboard():
    if request.method=='POST':
        #write a script to send email
        pass
    username=session['username']
    email=session['email'] 
    credits=Users.query.filter_by(email=email).first().credits
    
    
    return render_template("dash.html",username=username,credits=credits) 

@app.route('/pay', methods = ["POST","GET"])
@login_required
def pay():
    if request.method=='POST':
        number=request.form.get('phoneNumber')
        Pricing=request.form.get('plan')
        email=session['email'] 
        print(Pricing)

        publishable_key = "ISPubKey_live_6b6cfe86-303b-41f5-8152-022865f74d2f"

        service = APIService(publishable_key=publishable_key,token='ISSecretKey_live_dab2a24c-a5a6-4f50-8c6f-eb5c8948be9f')

        response = service.collect.mpesa_stk_push(phone_number='254'+number,
                                  email=email, amount=10, narrative="Purchase")
        print(response)
        
    username=session['username']
    email=session['email'] 
    credits=Users.query.filter_by(email=email).first().credits
    
    return render_template("payy.html",username=username,credits=credits) 

