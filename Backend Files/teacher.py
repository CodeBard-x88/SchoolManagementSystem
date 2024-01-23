from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from Users import Users
from database import create_app
from course import Course

app,db = create_app()

class Teacher(Users, db.Model):
    __tablename__ = 'teacher'

   # teacher_course_list=[]   #append only course_code
    qualifications = db.Column(db.String(50),nullable=False)
    teacher_class = db.Column(db.Integer, nullable=False)

    def __init__(self, name=None, username=None, password=None, email=None, phone=None, qualifications=None, teacher_class=None):
        super().__init__(name, username, password, email, phone)
        self.qualifications=qualifications
        self.teacher_class=teacher_class

    @classmethod
    def viewTeachers(cls):
        teachers = cls.query.all()
        headings = ['Name', 'Username', 'email', 'phone','Qualification','Class']

        # Format the data in a list of lists
        data = [[teacher.name, 
                 teacher.username, 
                 teacher.email, 
                 teacher.phone,
                 teacher.qualifications,
                 teacher.teacher_class
                 ] for teacher in teachers]

        return headings, data



