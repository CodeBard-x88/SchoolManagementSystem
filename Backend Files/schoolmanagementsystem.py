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
                admin_ = Admin(name=None, username=user, password=password_, email=None, contact_number=None)
                admin_.Login()
            except Exception as e:
                print(f"Exception: {e}")

sms = SchoolManagementSystem()  

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/admin_Login', methods=['GET', 'POST'])
def calladminLogin():
    if(request.method=='POST'):
       username= request.form['username']
       password = request.form['password']
       if username and password:        # validating that there is some input in the variables
            sms.adminLogin(username, password)
       else:     
            #Empty variable will redirect the user to login page
            return redirect(url_for('/admin_login'))

if __name__ == "__main__":
    app.run(debug=True)
    