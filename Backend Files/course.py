from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import create_app

app, db = create_app()

class Course(db.Model):
    
    __tablename__='courses'

    course_code = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    course_name = db.Column(db.String(50),primary_key=True,nullable=False)
    course_class = db.Column(db.Integer)
    course_fee = db.Column(db.Integer)

    def __init__(self,code=None,name=None,class_=None,fee=None):
        self.course_code=code
        self.course_name=name
        self.course_class=class_
        self.course_fee=fee

    def AddCoursetodb(self):
        query = db.session.query(self.__class__.course_code).filter_by(course_code=self.course_code)
        fetch = query.first()
        if fetch:
            return "Course code already exists!"
        try:
            db.session.add(self)
            db.session.commit()
            return "Course Added Successfully!"
        except Exception as e:
            print("Exception : {e}")
            return "Error Adding Course!"
        finally:
            db.session.close()

    
    @classmethod
    def ViewCourses(cls):
        courses = cls.query.all()
        headings = ['Course Code', 'Course Name', 'Class', 'Fee']  # Adjust these based on your actual column names

        # Format the data in a list of lists
        data = [[course.course_code, course.course_name, course.course_class, course.course_fee] for course in courses]

        return headings, data

    
