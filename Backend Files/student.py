from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, Column, Integer, String, PrimaryKeyConstraint
from Users import Users
from database import create_app
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

    #def setFeeConcession(self, fee_concession):
     #   self.fee_concession = fee_concession

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

    # def generateFeeChallan(self, month, fee_amount):
    #     # Assuming FeeChallan class has a method to generate a fee challan
    #     if not self.fee_challan:
    #         challan = FeeChallan(student=self, month=month, fee=fee_amount)
    #         db.session.add(challan)
    #         db.session.commit()

    # def getDetails(self):
    #     details = f"Student Details:\nName: {self.name}\nClass: {self.class_name}\nParent: {self.parent.getName()}\nPhone Number: {self.phone_number}\nAddress: {self.address}\nGender: {self.gender}\nFee Concession: {self.fee_concession}"
        
    #     if self.fee_challan:
    #         details += f"\n\nFee Challan Details:\n{self.fee_challan.viewChallanDetails()}"
    #     else:
    #         details += "\nNo fee challan generated."

    #     return details

    # def viewChallanDetails(self):
    #     # Assuming FeeChallan class has a method to view details
    #     if self.fee_challan:
    #         return self.fee_challan.viewChallanDetails()
    #     else:
    #         return "No fee challan generated."