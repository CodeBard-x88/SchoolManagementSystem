from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from database import create_app
from Users import Users
from sqlalchemy import text

app, db= create_app()

def remove_newlines(input_string):
    """Remove newline characters (\n) from the input string."""
    return input_string.replace('\n', '')


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
        self.tablename='admin'

    def Login(self):             
        try:

            if not db.session.is_active:        #In Case if database session is active or localhost is not working
                print("Database connection is not active.")
                return False
            
            #generating SQL query
            
            query = db.session.query(self.__class__).filter(self.__class__.username==self.user_name, self.__class__.password==self.user_password)
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

