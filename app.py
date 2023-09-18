

from flask import Flask, render_template, request, url_for, session,redirect,flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from model import *
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///studentadmin.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main():
    db.create_all()
   
    
    
if __name__ == "__main__":
    
    with app.app_context():

        main()
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/login")
def login():
    return render_template("SignIn.html")
@app.route("/register")
def register():
    return render_template("register.html")



@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "GET":
        return "Please submit the form"
    else:
        em = request.form.get("email")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        password = request.form.get("password")

        # lower_case = any(c.islower() for c in password)
        # upper_case = any(c.isupper() for c in password)
        # ends_with_digit = password[-1].isdigit()
        # password_length = len(password) >8
        # password_passed = lower_case and upper_case and ends_with_digit and password_length

        cpassword = request.form.get("cpassword")
        if cpassword == password:
            
            user = User(email=em,name=fname,lname=lname, password=password)
            db.session.add(user)
            db.session.commit()
            
        else:
            error = "Passwords do not match. Please type both the passwords correctly."
            
            return render_template("register.html",error=error,password=password)
        
            
            
        
        return render_template("Thankyou.html")
@app.route("/SignIn",methods=["POST"])
def SignIn():
    email = request.form.get("email")
    password = request.form.get("password")
    users = User.query.all()
    for user in users:
        if user.email == email :
            return render_template("secretpage.html",email=email)
        else:
            continue
    return render_template("test.html")