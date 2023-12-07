from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from Users import Users
from database import create_app
from course import Course

app,db = create_app()

class Teacher(Users, db.Model):
    __tablename__ = 'teachers'

    teacher_course_list=[]   #append only course_code
    qualification = db.Column(db.String(50),nullable=False)
    teacher_class = db.Column(db.Integer, nullable=False)

    def __init__(self, name=None, username=None, password=None, email=None, phone=None):
        super().__init__(name, username, password, email, phone)
