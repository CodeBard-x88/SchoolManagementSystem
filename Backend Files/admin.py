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
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    contact_number = db.Column(db.String(15), nullable=True)

    def __init__(self, name=None, username=None, password=None, email=None, contact_number=None):
        super().__init__(name, username, password, email, contact_number)

    def Login(self):
        print('Inside Admin class')
        sql = text('SELECT * FROM admin WHERE admin.username = :user_name AND admin.password = :user_password')
        print(self.user_name)
        print(self.user_password)

        try:
            print('Executing the query\n')
            found = db.session.execute(sql, {'user_name': self.user_name, 'user_password': self.user_password}).fetchone
        except Exception as e:
            print(f"Exception caught: {e}")
        finally:
            if found:
                print('Admin found')
                return render_template('admin.html')
            else:
                print('Admin not found')

