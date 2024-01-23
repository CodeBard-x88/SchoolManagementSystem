from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class marks(db.Model):
    __tablename__ = 'marks'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(255), nullable=False)
    class_number = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    exam = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    def __init__(self, student_id, class_number, subject, exam, number):
        self.student_id = student_id
        self.class_number = class_number
        self.subject = subject
        self.exam = exam
        self.number = number
