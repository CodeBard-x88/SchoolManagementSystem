from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database import db



class Users(db.Model):

    def __init__(self,name,username,password,email,phone):
        self.name_ = name
        self.user_name = username
        self.user_password = password
        self.user_email = email
        self.phone_num = phone

    def adminLogin(self):
        pass

    def GetUserName(self):
        return self.__user_name
    
    def GetUserId(self):
        return self.__user_id
    
    def GetUserPassword(self):
        return self.__user_password
    
    def GetUserEmail(self):
        return self.__user_email
