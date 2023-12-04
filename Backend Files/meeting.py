from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database import create_app

app,db = create_app()

class Meeting(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    is_canceled = db.Column(db.Boolean, default=False)

    teacher = db.relationship('Teacher', backref='meetings', lazy=True)
    parent = db.relationship('Parent', backref='meetings', lazy=True)

    def __init__(self, name, teacher, parent, time):
        self.name = name
        self.teacher = teacher
        self.parent = parent
        self.time = time

    def setName(self, name):
        self.name = name

    def setTeacher(self, teacher):
        self.teacher = teacher

    def setParent(self, parent):
        self.parent = parent

    def setTime(self, time):
        self.time = time

    def getName(self):
        return self.name

    def getTeacher(self):
        return self.teacher

    def getParent(self):
        return self.parent

    def getTime(self):
        return self.time

    def scheduleMeeting(self):
        self.is_canceled = False
        db.session.commit()

    def rescheduleMeeting(self, new_time):
        if not self.is_canceled:
            self.time = new_time
            db.session.commit()

    def cancelMeeting(self):
        self.is_canceled = True
        db.session.commit()

    def viewMeetingDetails(self):
        status = "Canceled" if self.is_canceled else "Scheduled"
        return f"Meeting Details:\nName: {self.name}\nTeacher: {self.teacher.getName()}\nParent: {self.parent.getName()}\nTime: {self.time}\nStatus: {status}"