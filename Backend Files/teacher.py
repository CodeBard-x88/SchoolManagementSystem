from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from Users import Users
from database import create_app

app,db = create_app()

class Teacher(Users, db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    section = db.Column(db.String(50), nullable=False)
    qualifications = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    courses = db.relationship('Course', backref='teacher', lazy=True)
    meetings = db.relationship('Meeting', backref='teacher', lazy=True)

    def __init__(self, name, section, qualifications, phone_number):
        self.name = name
        self.section = section
        self.qualifications = qualifications
        self.phone_number = phone_number

    def setName(self, name):
        self.name = name

    def setSection(self, section):
        self.section = section

    def setQualifications(self, qualifications):
        self.qualifications = qualifications

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    def getName(self):
        return self.name

    def getSection(self):
        return self.section

    def getQualifications(self):
        return self.qualifications

    def getPhoneNumber(self):
        return self.phone_number

    def assignCourse(self, course):
        # Assuming Course class has a teacher_id foreign key
        course.teacher_id = self.id
        db.session.commit()

    def viewStudentDetails(self, student):
        # Assuming Student class has a method to retrieve details
        return student.getDetails()

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
            print('Teacher found')
            return True
        else:
            print('Teacher not found')
        return False