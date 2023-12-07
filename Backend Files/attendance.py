from flask import Flask, render_template, request, url_for, redirect
from database import create_app
app, db = create_app()

class Attendance(db.Model):
    _tablename_ = 'attendance'

    student_id = db.Column(db.Integer, primary_skey=True)
    class_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def _init_(self, student_id=None, class_number=None, date=None, status=None):
        self.student_id = student_id
        self.class_number = class_number
        self.date = date
        self.status = status

    # def addAttendance(self):
    #     try:
    #         db.session.add(self)
    #         db.session.commit()
    #         return True
    #     except Exception as e:
    #         print(f"Exception: {e}")
    #         return False
        
    # def updateAttendance(self):
    #     try:
    #         db.session.commit()
    #         return True
    #     except Exception as e:
    #         print(f"Exception: {e}")
    #         return False
        
    # def deleteAttendance(self):
    #     try:
    #         db.session.delete(self)
    #         db.session.commit()
    #         return True
    #     except Exception as e:
    #         print(f"Exception: {e}")
    #         return False
        
    # def getAttendance(self):
    #     try:
    #         attendance = attendance.query.filter_by(student_id=self.student_id).first()
    #         return attendance
    #     except Exception as e:
    #         print(f"Exception: {e}")
    #         return False