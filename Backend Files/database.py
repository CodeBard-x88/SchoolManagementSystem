from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():

    """
    Connecting postgresql
    """

    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://avnadmin:AVNS_kayd37s41kGGRqSThn8@sms-school-management-system.a.aivencloud.com:10884/sms?sslmode=require'
    #app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/sms'
    db.init_app(app)
    print('database connected')
    return app,db

    """
    Following code was for mysql which created issue in querying
    """
    # app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:8080/ssms'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking, if not needed
    # db.init_app(app)
    # print ('database connected')
    # return app, db
