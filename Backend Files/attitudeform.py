from flask import Flask, render_template, request, url_for, redirect
from database import create_app
app, db = create_app()

class attitudeform(db.Model):
    __tablename__ =  'attitude_form'

    form_id = db.Column(db.Integer, primary_key=True)
    teacher_username = db.Column(db.String(50), nullable=False)
    class_number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_att =db.Column(db.Date, nullable=False)

    def _init_(self, form_id=None, teacher_username=None, class_number=None, description=None, date_att=None):
        self.form_id = form_id
        self.teacher_username = teacher_username
        self.class_number = class_number
        self.description = description
        self.date_att= date_att
    