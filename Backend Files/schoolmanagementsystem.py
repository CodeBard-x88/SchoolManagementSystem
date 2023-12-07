from flask import Flask, render_template, request, url_for, redirect
from database import create_app
from admin import Admin
from student import Student
from LeaveForm import LeaveForm
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
    
    def AddStudent(self,request_):
        name = request_.form['name']
        username = request_.form['username']
        password = request_.form['pssword']
        email = request_.form['email']
        phone =request_.form['phone']
        class_ = request_.form['class_']
        gender = request_.form['gender']
        parent_id = request_.form['parendID']
        address = request_.__form['address']
        parent_phone = request_.form['parentphone']
        return self.admin_.AddStudent(name,username,password,email,phone,class_,gender,parent_id,address,parent_phone)


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

@app.route('/submit_leave', methods=['POST'])
def submit_leave():
    if request.method == 'POST':
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        username = request.form['username']
        name = request.form['name']
        comments = request.form['comments']
        leave_type = request.form['leaveType']

        new_leave_form = LeaveForm(
            start_date=start_date,
            end_date=end_date,
            username=username,
            name=name,
            comments=comments,
            leave_type=leave_type
        )

        db.session.add(new_leave_form)
        db.session.commit()

        return redirect(url_for('index'))    #will redirect it later on to required page

@app.route('/admin_logout',methods=['GET','POST'])
def callLogout():
     sms.adminLogout()
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
        if sms.AddStudent(request):
            return LoadStudentForm("Student Added Successfully.")
        else:
            return LoadStudentForm("Student can't be added")
    else:
        # Handle GET request or other methods if needed
        return LoadStudentForm("Invalid request method")

     

if __name__ == "__main__":
    app.run(debug=True)


