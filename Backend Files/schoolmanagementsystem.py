from flask import Flask, render_template, request, url_for, redirect
from database import create_app
from admin import Admin
from student import Student
# from teacher import Teacher
# from parent import Parent

app, db = create_app()

class SchoolManagementSystem:
    
    __admin_ = None
    __student_= None
    __name = None
    def __init__(self):
        self.name = "School Management System"
        self.admin_ = Admin()
        self.student_=Student()

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
                boolean, studnet_ = temp.Login()        #here the student_ will be initialized and will perform the operations along this object
                return boolean
            except Exception as e:
                print(f"Exception: {e}")
                return False
    
    # def teacherLogin(self,user,password_): 
            
    #         try:
    #             print('creating teacher object')
    #             temp = Teacher(username=user, password=password_)
    #             boolean, teacher_ = temp.Login()        #here the teacher_ will be initialized and will perform the operations along this object
    #             return boolean
    #         except Exception as e:
    #             print(f"Exception: {e}")
    #             return False
            
    # def parentLogin(self,user,password_): 
            
    #         try:
    #             print('creating parent object')
    #             temp = Parent(username=user, password=password_)
    #             boolean, parent_ = temp.Login()        #here the parent_ will be initialized and will perform the operations along this object
    #             return boolean
    #         except Exception as e:
    #             print(f"Exception: {e}")
    #             return False

    def AddStudent(self,request_):
        name = request_.form['name']
        username = request_.form['username']
        password = request_.form['password']
        email = request_.form['email']
        phone =request_.form['phone']
        class_ = request_.form['class_']
        gender = request_.form['gender']
        parent_id = request_.form['parentID']
        address = request_.form['address']
        parent_phone = request_.form['parentphone']
        return self.admin_.AddStudent(name,username,password,email,phone,class_,gender,parent_id,address,parent_phone)

    def DeleteStudent(self, user):
        return self.admin_.DeleteStudent(user)

    def adminLogout(self):
         self.admin_=None

    def StudentLogout(self):
        self.student_=None

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
               return render_template("admin.html")         #if login is successful, admin dashboard is opened
       elif(user_type=='parent'):
            # if (sms.parentLogin(username, password)==True):
            #    return render_template("parentdash.html")       #if login is successful, parent dashboard is opened
            pass
       elif(user_type=='teacher'):
            # if (sms.teacherLogin(username, password)==True):
            #    return render_template("teadash.html")       #if login is successful, teacher dashboard is opened
            pass
       else:
            if (sms.StudentLogin(username, password)==True):
               return render_template("stddash.html")       #if login is successful, student dashboard is opened
       return LoadLoginPage("Incorrect Credentials!")

@app.route('/admin_logout',methods=['GET','POST'])
def callAdminLogout():
     sms.adminLogout()
     return LoadLoginPage("Logged Out!")

@app.route('/student_logout',methods=['GET','POST'])
def callStudentLogout():
     sms.StudentLogout()
     return LoadLoginPage("Logged Out!")

@app.route('/StudentForm')
def LoadStudentForm(message=None):
    return render_template('studentform.html',UI_message=message)

@app.route('/TeacherForm')
def LoadTeacherForm(message=None):
    return render_template('teacherForm.html',UI_message=message)

@app.route('/add_studnet', methods=['GET', 'POST'])
def add_Student():
    if request.method == 'POST':
        if sms.AddStudent(request):
            return LoadStudentForm("Student Added Successfully.")
        else:
            return LoadStudentForm("Student can't be added")
    else:
        # Handle GET request or other methods if needed
        return LoadStudentForm("Invalid request method")

@app.route('/deleteStudent',methods=['GET','POST'])
def delete_Student():
    if(request.method=='POST'):
        std_username = request.form['std_username']
        if sms.DeleteStudent(std_username):
            return LoadDelStudent("Student Successfully removed.")
        else:
            return LoadDelStudent(f"Student with username {std_username} does not exist!")
    
@app.route('/render_delstd')
def LoadDelStudent(message=None):
    return render_template('delstd.html',UI_message=message)

@app.route('/render_admindash')
def LoadAdminDash():
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)

