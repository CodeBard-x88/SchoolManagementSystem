from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from Users import Users
from database import create_app
from FeeChallan import FeeChallan

app,db = create_app()

class Student(Users, db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    fee_concession = db.Column(db.Float, default=0.0)
    
    # Directly include a reference to the FeeChallan
    fee_challan = db.relationship('FeeChallan', backref='student', uselist=False, lazy=True)

    def __init__(self, name, class_name, parent, phone_number, address, gender, fee_concession=0.0):
        self.name = name
        self.class_name = class_name
        self.parent = parent
        self.phone_number = phone_number
        self.address = address
        self.gender = gender
        self.fee_concession = fee_concession

    def setName(self, name):
        self.name = name

    def setClass(self, class_name):
        self.class_name = class_name

    def setParent(self, parent):
        self.parent = parent

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    def setAddress(self, address):
        self.address = address

    def setGender(self, gender):
        self.gender = gender

    def setFeeConcession(self, fee_concession):
        self.fee_concession = fee_concession

    def getName(self):
        return self.name

    def getClass(self):
        return self.class_name

    def getParent(self):
        return self.parent

    def getPhoneNumber(self):
        return self.phone_number

    def getAddress(self):
        return self.address

    def getGender(self):
        return self.gender

    def getFeeConcession(self):
        return self.fee_concession

    def generateFeeChallan(self, month, fee_amount):
        # Assuming FeeChallan class has a method to generate a fee challan
        if not self.fee_challan:
            challan = FeeChallan(student=self, month=month, fee=fee_amount)
            db.session.add(challan)
            db.session.commit()

    def getDetails(self):
        details = f"Student Details:\nName: {self.name}\nClass: {self.class_name}\nParent: {self.parent.getName()}\nPhone Number: {self.phone_number}\nAddress: {self.address}\nGender: {self.gender}\nFee Concession: {self.fee_concession}"
        
        if self.fee_challan:
            details += f"\n\nFee Challan Details:\n{self.fee_challan.viewChallanDetails()}"
        else:
            details += "\nNo fee challan generated."

        return details

    def viewChallanDetails(self):
        # Assuming FeeChallan class has a method to view details
        if self.fee_challan:
            return self.fee_challan.viewChallanDetails()
        else:
            return "No fee challan generated."