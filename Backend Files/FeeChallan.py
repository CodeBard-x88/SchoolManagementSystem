from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database import create_app

app,db = create_app()

class FeeChallan(db.Model):
    __tablename__ = 'fee_challan'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    fee = db.Column(db.Float, nullable=False)
    is_paid = db.Column(db.Boolean, default=False)

    def __init__(self, student, month, fee):
        self.student = student
        self.month = month
        self.fee = fee

    def setStudent(self, student):
        self.student = student

    def setMonth(self, month):
        self.month = month

    def setFee(self, fee):
        self.fee = fee

    def getStudent(self):
        return self.student

    def getMonth(self):
        return self.month

    def getFee(self):
        return self.fee

    def payChallan(self):
        self.is_paid = True
        db.session.commit()

    def viewChallanDetails(self):
        status = "Paid" if self.is_paid else "Pending"
        return f"Challan Details:\nStudent: {self.student.getName()}\nMonth: {self.month}\nFee: {self.fee}\nStatus: {status}"