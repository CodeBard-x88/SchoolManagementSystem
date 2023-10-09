from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

app = Flask(__name__)
engine= create_engine("sqlite:///mydb.db", echo=True)  #creates a sqlite database 

Session = sessionmaker(bind=engine)     #creates a sqlite database session
db= Session()        #creating a database object


class Users:

    def __init__(self,name,id,password,email):
        __user_name = name
        __user_id = id
        __user_password = password
        __user_email = email

    def GetUserName(self):
        return self.__user_name
    
    def GetUserId(self):
        return self.__user_id
    
    def GetUserPassword(self):
        return self.__user_password
    
    def GetUserEmail(self):
        return self.__user_email


class Admin(Users,Base):
    pass

class Students(Users,Base):
    pass

class Teachers(Users,Base):
    pass

class Parents(Users,Base):
    pass