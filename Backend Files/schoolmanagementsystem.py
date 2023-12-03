from flask import Flask, render_template
from database import db

app = Flask(__name__)
class SchoolManagementSystem:

    def __init__(self):
        self.name = "School Management System"


sms = SchoolManagementSystem()   #an instance of school management system

@app.route('/')
def hello_world():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
    