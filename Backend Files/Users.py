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

    def Login(self):
        try:

            if not db.session.is_active:        #In Case if database session is active or localhost is not working
                print("Database connection is not active.")
                return False
            
            #generating SQL query
            
            query = db.session.query(self.__class__).filter(self.__class__.username==self.user_name, self.__class__.password==self.user_password)
            print(str(query))
            found = query.first()  #executes the generated sql query
            db.session.close()
        except Exception as e:
            print(f"Exception caught: {e}")
            found = None  # Set found to None in case of an exception

        finally:
            if found:
                print('Admin found')
                return True
            else:
                print('Admin not found')
        return False
