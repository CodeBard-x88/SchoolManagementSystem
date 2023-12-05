from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from database import create_app
from Users import Users
from sqlalchemy import text

app, db= create_app()

class Admin(Users, db.Model):

    """
    Defining the table structure in database
    """
    __tablename__ = 'admin'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    contact_number = db.Column(db.String(15), nullable=True)

    def __init__(self, name=None, username=None, password=None, email=None, contact_number=None):
        super().__init__(name, username, password, email, contact_number)


