from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database import create_app

app,db = create_app()

class Users(db.Model):
    __abstract__ = True

    name = db.Column(db.String(255))
    username = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(15), nullable=True)

    def __init__(self, name=None, username=None, password=None, email=None, phone=None):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    def Login(self):
        try:
            query = db.session.query(self.__class__).filter(
                self.__class__.username == self.username,
                self.__class__.password == self.password
            )
            found = query.first()
        except Exception as e:
            print(f"Exception caught: {e}")
            found = None
        finally:
            db.session.close()

        if found:
            print(f'{self.__class__.__name__} found')
            return True, found
        else:
            print(f'{self.__class__.__name__} not found')
            return False

    def Logout(self):
        pass

    

