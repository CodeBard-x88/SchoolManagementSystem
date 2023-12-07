from flask import Flask, render_template, request, url_for, redirect
from database import create_app
app, db = create_app()

class LeaveForm(db.Model):
    __tablename__ =  'LeaveForm'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    leave_type = db.Column(db.String(20), nullable=False)