from flask import Flask, render_template
from database import db
from admin import Admin

app = Flask(__name__)
class SchoolManagementSystem:

    def __init__(self):
        self.name = "School Management System"

    def adminLogin(self):
        admin_ = Admin()
        admin_.Login()



sms = SchoolManagementSystem()   #an instance of school management system

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/admin_Login')
def calladminLogin():
    sms.adminLogin()

if __name__ == "__main__":
    app.run(debug=True)
    