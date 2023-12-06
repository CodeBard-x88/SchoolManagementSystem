from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from database import create_app
from Users import Users
from student import Student

app, db= create_app()

class Admin(Users, db.Model):
    """
    Defining the table structure in the database
    """
    __tablename__ = 'admin'
    #contact_number = db.Column(db.String(15), nullable=True)

    def __init__(self, name=None, username=None, password=None, email=None, contactnumber=None):
        super().__init__(name, username, password, email, phone=contactnumber)
    def AddStudent(self, name, username, password, email, phone, class_, gender, parent_id, address, parent_phone):
     try:
        # Use the parameters passed to the method instead of attributes from Admin
        std = Student(name=name, username=username, password=password, email=email, phone=phone, enrolled_class=class_, Gender=gender, parent_ID=parent_id, address=address, parent_contact=parent_phone)
        db.session.add(std)
        db.session.commit()
        return True
     except Exception as e:
        print(f"Error during commit: {e}")
        db.session.rollback()
        return False
     finally:
        db.session.close()


