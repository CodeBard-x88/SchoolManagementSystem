from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

class Users():

    def __init__(self,name,username,password,email,phone):
        self.name_ = name
        self.user_name = username
        self.user_password = password
        self.user_email = email
        self.phone_num = phone

    def Login(self):
        pass