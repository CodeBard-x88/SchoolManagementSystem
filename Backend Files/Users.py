from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database import create_app

app,db = create_app()

class Users():

    __tablename__ = 'admin'
    def __init__(self,name,username,password,email,phone):
        self.name_ = name
        self.user_name = username
        self.user_password = password
        self.user_email = email
        self.phone_num = phone

    def Login(self):
        pass