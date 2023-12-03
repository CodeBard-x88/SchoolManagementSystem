from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:8080/ssms'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking, if not needed
    
    db.init_app(app)
    print ('database connected')
    return app, db

# app = Flask(__name__, static_folder='static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:8080/ssms'
# try:
#     # Attempt to create the SQLAlchemy object and bind it to the app
#     db = SQLAlchemy(app)
#     print ('database connected')
# except Exception as e:
#     print(f"Error creating SQLAlchemy object: {e}")
#     db = None

# class Admin(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(255), nullable=True)
#     contact_number = db.Column(db.String(15), nullable = True)
