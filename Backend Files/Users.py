from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database import create_app

app,db = create_app()

class Users():

    def __init__(self,name,username,password,email,phone):
        self.name_ = name
        self.user_name = username
        self.user_password = password
        self.user_email = email
        self.phone_num = phone

    def Login(self,table_name):
        try:
            # sql = text(f'SELECT * FROM {table_name} WHERE username = :user_name AND password = :user_password')
            # found = db.session.execute(sql, {'user_name': self.user_name, 'user_password': self.user_password}).fetchone()
            #found = db.session.query(self.__class__).filter_by(username=self.user_name, password=self.user_password).first()
            found=self.query.filter_by(username=self.user_name, password=self.user_password)  #matching the username and password in the database
        except Exception as e:
            print(f"Exception caught:{e}")
        finally:
            db.session.close()
        if found is not None:
            print('Admin found')
            return True
        else:
            print('Admin not found')
        return False