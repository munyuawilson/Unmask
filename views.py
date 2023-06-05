from flask import request,render_template,redirect,session

from model import Users,db,Conmen
from main import app



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
        image=request.files['image']
        
        new_con=Conmen(name=name,number=number,email=email,social_media=social_media,reason=reason, image=image.read())
        db.session.add(new_con)
        db.session.commit()

        
        
    return render_template('add.html')
@app.route('/search',methods = ['POST',"GET"])
def search():
    pass
        

    return render_template("search.html")

@app.route('/logout',methods=["POST","GET"])
def logout():
    pass
    return redirect("/")

@app.route('/', methods = ["POST","GET"])
def home():
    if request.method=='POST':
        #write a script to send email
        pass

    return render_template("main.html")
    
@app.route('/dashboard', methods = ["POST","GET"])
def dashboard():
    if request.method=='POST':
        #write a script to send email
        pass
    name=session['username']
    
    return render_template("dashboard.html",name=name) 

@app.route('/pay', methods = ["POST","GET"])
def pay():
    if request.method=='GET':
        #write a script to send email
        pass

    return render_template("pay.html") 

