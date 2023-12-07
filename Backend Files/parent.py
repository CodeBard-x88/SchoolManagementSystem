from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, Column, Integer, String, PrimaryKeyConstraint
from Users import Users
from database import create_app

app,db = create_app()

class Parent(Users, db.Model):

    __tablename__ = 'parent'

    def __init__(self, name=None, username=None, password=None, email=None, phone=None):
        super().__init__(name, username, password, email, phone)

    
    
    