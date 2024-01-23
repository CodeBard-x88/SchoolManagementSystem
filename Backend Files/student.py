from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, Column, Integer, String, PrimaryKeyConstraint
from Users import Users
from database import create_app
from passwordGenerator import GetaPassword
from parent import Parent
from LeaveForm import LeaveForm
#from FeeChallan import FeeChallan

app,db = create_app()

class Student(Users):
    __tablename__ = 'student'

    enrolled_class = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.String(255), nullable=False)
    parent_ID = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    parent_contact = db.Column(db.String(50), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    parent_email = db.Column(db.String(255), nullable=False)

    def __init__(self, name=None, username=None, password=None, email=None, phone=None,
                 enrolled_class=None, Gender=None, parent_ID=None, address=None, parent_contact=None,pname=None,pemail=None):
        super().__init__(name, username, password, email, phone)
        self.enrolled_class = enrolled_class
        self.Gender = Gender
        self.parent_ID = parent_ID
        self.address = address
        self.parent_contact = parent_contact
        self.parent_email=pemail
        self.parent_name=pname

    
    @classmethod
    def ViewStudents(cls):
        students = cls.query.all()
        headings = ['Name', 'Username', 'email', 'phone','Enrolled Class', 'Gender','Parent Id','Address','Parent Contact','Parent Name','Parent Email']  # Adjust these based on your actual column names

        # Format the data in a list of lists
        data = [[student.name, 
                 student.username, 
                 student.email, 
                 student.phone,
                 student.enrolled_class,
                 student.Gender,
                 student.parent_ID,
                 student.address,
                 student.parent_contact,
                 student.parent_name,
                 student.parent_email
                 ] for student in students]

        return headings, data

    def submit_leave_form(self, start_date, end_date, description, leave_type, username1, name1):
                new_leave_form = LeaveForm(
                    start_date=start_date,
                    end_date=end_date,
                    username=username1,
                    name=name1,
                    description=description,
                    leave_type=leave_type
                )

                db.session.add(new_leave_form)
                db.session.commit()
                db.session.close()

                return render_template('stddash.html')
