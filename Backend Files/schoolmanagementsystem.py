from flask import Flask, render_template, request, url_for, redirect
from database import create_app
from admin import Admin
from student import Student
app, db = create_app()

class SchoolManagementSystem:
    
    __admin_ = None
    __student_= None
    __name = None
    def __init__(self):
        self.name = "School Management System"
        self.admin_ = None
        self.student_=None

    def adminLogin(self,user,password_): 
            
            try:
                print('creating admin object')
                temp = Admin(username=user, password=password_)
                boolean, admin_ = temp.Login()        #here the admin_ will be initialized and will perform the operations along this object
                return boolean
            except Exception as e:
                print(f"Exception: {e}")
                return False
    
    def StudentLogin(self,user,password_): 
            
            try:
                print('creating Student object')
                temp = Student(username=user, password=password_)
                boolean, student_ = temp.Login()        #here the student_ will be initialized and will perform the operations along this object
                return boolean
            except Exception as e:
                print(f"Exception: {e}")
                return False

    def adminLogout(self):
         self.admin_=None

sms = SchoolManagementSystem()  

@app.route('/')
def LoadLoginPage(message=None):
    return render_template("login.html",UI_message=message)

@app.route('/admin_Login', methods=['GET', 'POST'])
def callLogin():

    if(request.method=='POST'):
       user_type = request.form['user_type']
       username= request.form['username']
       password = request.form['password']
       if(user_type=='admin'):
           if (sms.adminLogin(username, password)==True):
               return render_template("admin.html")         #if login is successful, dashboard is opened
       elif(user_type=='parent'):
             pass
       elif(user_type=='teacher'):
             pass
       else:
            if (sms.StudentLogin(username, password)==True):
               return render_template("stddash.html")
       return LoadLoginPage("Incorrect Credentials!")


@app.route('/admin_logout',methods=['GET','POST'])
def callLogout():
     sms.adminLogout()
     return LoadLoginPage("Logged Out!")
()

if __name__ == "__main__":
    app.run(debug=True)


