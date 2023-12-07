from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import create_app

app, db = create_app()

class Course(db.Model):
    
    __tablename__='courses'

    course_code = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    course_name = db.Column(db.String(50),primary_key=True,nullable=False)
    course_class = db.Column(db.Integer)
    course_fee = db.Column(db.Integer)

    def __init__(self,code=None,name=None,fee=None):
        self.course_code=code
        self.course_name=name
        self.course_fee=fee
