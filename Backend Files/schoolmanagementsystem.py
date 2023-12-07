from flask import Flask, render_template, request, url_for, redirect, session
from database import create_app
from admin import Admin
from student import Student
from teacher import Teacher
from LeaveForm import LeaveForm
from parent import Parent

app, db = create_app()
app.secret_key = 'your_secret_key'

class SchoolManagementSystem:
    
    admin_ = None
    student_= None
    name = None
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
                boolean, studnet_ = temp.Login()
                if boolean:
                    session['student'] = {
                    'username': studnet_.username,
                    'name': studnet_.name,
                }        #here the student_ will be initialized and will perform the operations along this object
                return boolean
            except Exception as e:
                print(f"Exception: {e}")
                return False
    
    
    def teacherLogin(self,user,password_):
            try:
                print('creating teacher object')
                temp = Teacher(username=user, password=password_)
                boolean, teacher_ =temp.Login()
                return boolean
            except Exception as e:
                print(f"Exception: {e}")
                return False
            
            

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
        parentname = request.form['parentname']
        parentemail = request.form['parentemail']
        return self.admin_.AddStudent(name,username,password,email,phone,class_,gender,parent_id,address,parent_phone,parentname,parentemail)

    def DeleteStudent(self, user):
        return self.admin_.DeleteStudent(user)

    def adminLogout(self):
         self.admin_=None

    def StudentLogout(self):
        self.student_=None

    def AddCourse(self,request_):
        code = request_.form['coursecode']
        name = request_.form['coursename']
        class_ = request_.form['courseclass']
        fee = request_.form['coursefee']
        return self.admin_.AddNewCourse(code,name,class_,fee)
    
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
             if (sms.parentLogin(username, password)==True):
                return render_template("parentdash.html")       #if login is successful, parent dashboard is opened
       elif(user_type=='teacher'):
            if (sms.teacherLogin(username, password)==True):
               return render_template("teadash.html")       #if login is successful, teacher dashboard is opened
       else:
            if (sms.StudentLogin(username, password)==True):
               return render_template("stddash.html")       #if login is successful, student dashboard is opened
       return LoadLoginPage("Incorrect Credentials!")

@app.route('/submit_leave', methods=['POST'])
def submit_leave():
    if request.method == 'POST':
        if 'student' in session:
            start_date = request.form['startDate']
            end_date = request.form['endDate']
            description = request.form['description']
            leave_type = request.form['leaveType']

            new_leave_form = LeaveForm(
                start_date=start_date,
                end_date=end_date,
                username=session['student']['username'],
                name=session['student']['name'],
                description=description,
                leave_type=leave_type
            )

            db.session.add(new_leave_form)
            db.session.commit()
            db.session.close()

            return render_template('stddash.html')

        return LoadLoginPage("Session expired. Please log in again.")    #will redirect it later on to required page

@app.route('/admin_logout',methods=['GET','POST'])
def callAdminLogout():
     sms.adminLogout()
     return LoadLoginPage("Logged Out!")

@app.route('/fee_concession', methods = ['GET', 'POST'])
def fee_concession():
    return render_template('feeconcession.html')

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

@app.route('/leaveform')
def leave_form():
    return render_template('leaveform.html')

@app.route('/add_studnet', methods=['GET', 'POST'])
def add_Student():
    if request.method == 'POST':
        boolean, msg = sms.AddStudent(request)
        if boolean:
            return LoadStudentForm(msg)
        else:
            return LoadStudentForm(msg)
    else:
        # Handle GET request or other methods if needed
        return LoadStudentForm("Invalid request method")

@app.route('/render_addcourse')
def LoadAddStudent(message=None):
    return render_template('addcourse.html',UI_message=message)

@app.route('/addcourse',methods=['GET','POST'])
def addnewCourse():
    if request.method=='POST':
        msg = sms.AddCourse(request)
        return LoadAddStudent(msg)


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