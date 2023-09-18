
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__="details"
    id = db.Column(db.Integer)
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    name = db.Column(db.String(80),nullable=False)
    lname = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(500),nullable=False)
    # mobile = db.Column(db.String(80),nullable=False)
    # dob = db.Column(db.String,nullable=False)
    
    # gender = db.Column(db.String(8),nullable=False)
    # timestamp = db.Column(db.DateTime, nullable=False)



# def __init__(self,email,name,password):
#     self.email = email
#     self.name = name
#     self.password = password
#     self.mobile = mobile
#     self.dob = dob
    
#     self.gender = gender
#     self.timestamp = timestamp

# class Student(db.Model):
#     __tablename__="student_details"
#     id = db.Column(db.Integer,primary_key=True)
    
#     fname = db.Column(db.String(80),nullable=False)
#     lname = db.Column(db.String(80),nullable=False)
#     mobile = db.Column(db.String(80),nullable=False)
#     email = db.Column(db.String(120),nullable=False)
#     dob = db.Column(db.String,nullable=False)
#     gender = db.Column(db.String(8),nullable=False)
#     qual = db.Column(db.String(40),nullable=False)
#     python = db.Column(db.String(10),nullable=True)
#     dotnet = db.Column(db.String(10),nullable=True)
#     java = db.Column(db.String(10),nullable=True)
#     database = db.Column(db.String(10),nullable=True)
#     image = db.Column(db.String(20), unique=True, nullable=False)
#     img_name = db.Column(db.String(20), nullable=False)
#     mimetype = db.Column(db.Text, nullable=False)
#     des = db.Column(db.String(600),nullable=False)
# # def __init__(self,fname,lname,mobile,email,dob,gender,qual,python,dotnet,java,database,image,img_name,mimetype,des):
    
# #     self.fname = fname
# #     self.lname=lname
    
# #     self.mobile = mobile
# #     self.email = email
# #     self.dob = dob
    
# #     self.gender = gender
# #     self.qual = qual
# #     self.python = python
# #     self.dotnet=dotnet
# #     self.java=java
# #     self.database=database
# #     self.image=image
# #     self.img_name=img_name
# #     self.mimetype=mimetype
# #     self.des=des



