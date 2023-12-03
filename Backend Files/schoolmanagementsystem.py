from flask import Flask, render_template, request
from admin import Admin

app = Flask(__name__)

class SchoolManagementSystem:

    def __init__(self):
        self.name = "School Management System"

    def adminLogin(self,user,password_):
        print('creating admin object')
        admin_ = Admin(name=None,username=user,password=password_,email=None,phone=None)
        admin_.Login()

sms = SchoolManagementSystem()  

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/admin_Login', methods=['GET', 'POST'])
def calladminLogin():
    if(request.method=='POST'):
       username= request.form['username']
       password = request.form['password']
       sms.adminLogin(username,password)

if __name__ == "__main__":
    app.run(debug=True)
    