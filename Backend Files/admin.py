from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from database import create_app
from Users import Users
from student import Student
from parent import Parent
from passwordGenerator import GetaPassword

app, db= create_app()

class Admin(Users, db.Model):
    """
    Defining the table structure in the database
    """
    __tablename__ = 'admin'
    #contact_number = db.Column(db.String(15), nullable=True)

    def __init__(self, name=None, username=None, password=None, email=None, contactnumber=None):
        super().__init__(name, username, password, email, phone=contactnumber)

    def AddStudent(self, name, username, password, email, phone, class_, gender, parent_id, address, parent_phone,p_name,p_email):
     try:
        query = db.session.query(Student).filter(Student.username==username)
        found = query.first()
        if found:
           return False, "Username already exists!"
        std = Student(name=name, username=username, password=password, email=email, phone=phone, enrolled_class=class_, Gender=gender, parent_ID=parent_id, address=address, parent_contact=parent_phone,pname=p_name,pemail=p_email)
        db.session.add(std)
        #db.session.commit()

        #creating account for parents with the parent_id provided by student form
        std_parent = Parent(std.parent_name,std.parent_ID,GetaPassword(),std.parent_email,std.parent_contact)
        db.session.add(std_parent)
        db.session.commit()
        return True , "Student added Successfully!"
     except Exception as e:
        print(f"Error during commit: {e}")
        db.session.rollback()
        return False , "Unable to add student!"
     finally:
        db.session.close()
    
    def DeleteStudent(self,id):
        try:
            result = db.session.query(Student).filter_by(username=id)
            std = result.first()
            if std:
               db.session.delete(std)
               db.session.commit()
               return True
            return False
        except Exception as e:
           print('Exception : {e}')
           return False
        finally:
           db.session.close()
          
       

