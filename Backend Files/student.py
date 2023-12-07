from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, Column, Integer, String, PrimaryKeyConstraint
from Users import Users
from database import create_app
from passwordGenerator import GetaPassword
from parent import Parent
#from FeeChallan import FeeChallan

app,db = create_app()

class Student(Users):
    __tablename__ = 'student'

    enrolled_class = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.String(255), nullable=False)
    parent_ID = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    parent_contact = db.Column(db.String(50), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    parent_email = db.Column(db.String(255), nullable=False)

    def __init__(self, name=None, username=None, password=None, email=None, phone=None,
                 enrolled_class=None, Gender=None, parent_ID=None, address=None, parent_contact=None,pname=None,pemail=None):
        super().__init__(name, username, password, email, phone)
        self.enrolled_class = enrolled_class
        self.Gender = Gender
        self.parent_ID = parent_ID
        self.address = address
        self.parent_contact = parent_contact
        self.parent_email=pemail
        self.parent_name=pname

 
