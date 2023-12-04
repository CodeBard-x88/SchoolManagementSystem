from flask import Flask, render_template, request, url_for, redirect
from database import create_app
from admin import Admin

app, db = create_app()

class SchoolManagementSystem:
    
    def __init__(self):
        self.name = "School Management System"

    def adminLogin(self,user,password_):
            try:
                print('creating admin object')
                admin_ = Admin(username=user, password=password_)
                return admin_.Login('admin')
            except Exception as e:
                print(f"Exception: {e}")
                return False

sms = SchoolManagementSystem()  

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/admin_Login', methods=['GET', 'POST'])
def calladminLogin():
    if(request.method=='POST'):
       username= request.form['username']
       password = request.form['password']
       if (sms.adminLogin(username, password)==True):
           return render_template("admin.html")         #if login is successful, dashboard is opened
       else:
           hello_world()

if __name__ == "__main__":
    app.run(debug=True)
    