from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, Column, Integer, String, PrimaryKeyConstraint
from Users import Users
from database import create_app

app,db = create_app()

class Parent(Users):

    __tablename__ = 'parent'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    #fee_concession = db.Column(db.String(255), nullable=False)
    students = db.relationship('Student', backref='parent', lazy=True)

    def __init__(self, name=None, username=None, password=None, email=None, phone=None,
                 student_id=None, address=None, phone_number=None):
        super().__init__(name, username, password, email, phone)
        self.student_id = student_id
        self.address = address
        self.phone_number = phone_number
        #self.fee_concession = fee_concession

    def setName(self, name):
        self.name = name
    
    def setStudent(self, student):
        self.student = student
    
    def setAddress(self, address):
        self.address = address

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    #def setFeeConcession(self, fee_concession):
        #   self.fee_concession = fee_concession

    def getName(self):
        return self.name
    
    def getStudent(self):
        return self.student
    
    def getAddress(self):
        return self.address
    
    def getPhoneNumber(self):
        return self.phone_number
    
    #def getFeeConcession(self):
        #   return self.fee_concession

    def Login(self,table_name):
        try:
            user = table_name.query.filter_by(username=self.username).first()
            if user:
                if user.password == self.password:
                    return True, user
                else:
                    return False, None
            else:
                return False, None
        except Exception as e:
            print(f"Exception: {e}")
            return False, None
        finally:
            db.session.close()
    
    