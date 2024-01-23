from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from database import create_app
from admin import Admin
from student import Student
from teacher import Teacher
from LeaveForm import LeaveForm
from course import Course
from attendance import Attendance
from marks import marks
from attitudeform import attitudeform
from parent import Parent
from FeeChallan import FeeChallan
import os
from sqlalchemy.sql import func



app, db = create_app()
app.secret_key = 'your_secret_key'

class SchoolManagementSystem:
    
    admin_ = None
    student_= None
    parent_= None
    name = None
    teacher_ = None
    fee_concession = None
    fee_challan_obj = None

    def __init__(self):
        self.name = "School Management System"
        self.admin_ = Admin()
        self.student_=Student()
        self.parent_=Parent()
        self.teacher_=Teacher()
      #  self.fee_concession = FeeConcession()

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
                    'enrolled_class': studnet_.enrolled_class,

                }        #here the student_ will be initialized and will perform the operations along this object
                return boolean
            except Exception as e:
                print(f"Exception: {e}")
                return False
            
    def parentLogin(self,user,password_): 
            
            try:
                print('creating parent object')
                temp = Parent(username=user, password=password_)
                boolean, parent_ = temp.Login()
                if boolean:
                    session['parent'] = {
                    'username': parent_.username,
                    'name': parent_.name
                }        #here the parent_ will be initialized and will perform the operations along this object
                return boolean
            except Exception as e:
                print(f"Exception: {e}")
                return False
                
    
    def teacherLogin(self,user,password_):
            try:
                print('creating teacher object')
                temp = Teacher(username=user, password=password_)
                boolean, teacher_ =temp.Login()
                if boolean:
                    session['teacher'] = {
                    'username': teacher_.username,
                    'name': teacher_.name,
                    'teacher_class': teacher_.teacher_class
                    # Add other relevant information
                }
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

    def GetCoursesList(self):
        return Course.ViewCourses()
    
    def GetStudentsList(self):
        return Student.ViewStudents()
    
    def GetTeachersList(self):
         return Teacher.viewTeachers()
    
    def GetParentsList(self):
         return Parent.ViewParents()
    
    def adminLogout(self):
         self.admin_=None

    def StudentLogout(self):
        self.student_=None

    from sqlalchemy import func

    def submit_fee_challan(self, request_):
        if request.method == 'POST':
            if 'student' in session:
                student_id = session['student']['username']  # You need to adjust this based on your actual session structure
                name = session['student']['name']
                month = request_.form['month']

                # Calculate the total fee using SQLAlchemy
                total_fee = db.session.query(func.sum(Course.course_fee)).scalar()

                # Create a new FeeChallan instance and store it in the database
                return self.admin_.calculate_fee_challan(student_id, name, month, total_fee)

    def submit_leave_req(self, request_):
        if request.method == 'POST':
            if 'student' in session:
                start_date = request_.form['startDate']
                end_date = request_.form['endDate']
                description = request_.form['description']
                leave_type = request_.form['leaveType']
                username=session['student']['username']
                name=session['student']['name']
                return self.student_.submit_leave_form(start_date, end_date, description, leave_type, username, name)
    
    def submit_fee_concession1(self, request_):
        if request.method == 'POST':
            if 'student' in session:
                reason = request_.form['reason']
                additional_details = request_.form['details']
                username = session['student']['username']
                name = session['student']['name']


                return self.fee_concession.submit_fee_concession2(reason, additional_details, username, name)
            

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


@app.route('/add_attitude',methods=['GET','POST'])
def addattitude():
      print('adding attitude')
      return render_template('classATT.html')
  


@app.route('/submit_attitude', methods=['POST'])
def submit_attitude():
    if request.method == 'POST':
        
        date_att = request.form['Date']
        description = request.form['comments']
       
        new_attitude_form = attitudeform(
            
            teacher_username=session['teacher']['username'],
            class_number=session['teacher']['teacher_class'],
            description=description,
            date_att =date_att,
        )

        db.session.add(new_attitude_form)
        db.session.commit()
        db.session.close()

        return render_template('teadash.html')



  
@app.route('/add_attendance',methods=['GET','POST'])
def addattendance():
      print('adding attendance')
      students = Student.query.filter_by(enrolled_class=session['teacher']['teacher_class']).all()
      return render_template('uploadattendance.html', students=students)
  
  
@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    if request.method == 'POST':
        if 'teacher' in session:
            status = [request.form['status']]
            date = request.form['Date']
            students = Student.query.filter_by(enrolled_class=session['teacher']['teacher_class']).all()
            for studentt in students:
                new_attendance = Attendance(
                    student_id = studentt.username,
                    class_number= session['teacher']['teacher_class'],
                    date= date,
                    status=status,
                )

                db.session.add(new_attendance)
                db.session.commit()



            db.session.close()
            return render_template('teadash.html')  

        return render_template('teadash.html')  
  
@app.route('/add_marks',methods=['GET','POST'])
def addmarks():
    print('adding marks')
    students = Student.query.filter_by(enrolled_class=session['teacher']['teacher_class']).all()
    return render_template('uploadmarks.html', students=students)

@app.route('/submit_marks', methods=['POST'])
def submit_marks():
    if request.method == 'POST':
        if 'student' in session:
            exam = [request.form['exam']]
            number = [request.form['number']]
            subject = request.form['subject']
            
            new_mark = marks(
                student_id = session['student']['username'],
                class_number= session['teacher']['teacher_class'],
                subject=subject,
                exam=exam,
                number=number,
              
            )

            db.session.add(new_mark)
            db.session.commit()
            db.session.close()
            
            return render_template('teadash.html')  

        return render_template('teadash.html')  

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

@app.route('/select_courses', methods=['GET', 'POST'])
def select_courses():
    if request.method == 'POST':
        selected_class = request.form.get('selected_class')

        # Query courses based on the selected class
        courses = Course.query.filter_by(course_class=selected_class).all()

        # Prepare course data for the dropdown menu
        course_data = [{'code': course.course_code, 'name': course.course_name} for course in courses]

        return jsonify({'courses': course_data})

    # Render the HTML template with the form
    return render_template('select_courses.html')

@app.route('/renderviewcourses')
def viewCourses():
    headings,data=sms.GetCoursesList()
    return render_template('viewtable.html', headings=headings, data=data)

@app.route('/renderviewstudents')
def viewStudents():
            headings,data=sms.GetStudentsList()
            return render_template('viewtable.html',headings=headings,data=data)

@app.route('/renderviewteachers')
def viewTeachers():
            headings,data=sms.GetTeachersList()
            return render_template('viewtable.html',headings=headings,data=data)

@app.route('/fee_concession', methods = ['GET', 'POST'])
def fee_concession1():
    return render_template('feeconcession.html')

@app.route('/fee_challan')
def fee_challan_page():
    return render_template('fee_challan.html')


@app.route('/leaveform')
def leave_form():
    return render_template('leaveform.html')

@app.route('/submit_leave', methods=['POST'])
def submit_leave():
    return sms.submit_leave_req(request)

@app.route('/submit_fee_concession', methods=['POST'])
def submit_fee_concession():
    return sms.submit_fee_concession1(request)

@app.route('/view_courses')
def view_courses():
    courses_data = Course.query.all()
    return render_template('viewCourses.html', courses_data=courses_data)

@app.route('/create_challan', methods=['GET', 'POST'])
def create_challan():
    return sms.submit_fee_challan(request)


@app.route('/renderviewparents')
def viewParents():
            headings,data=sms.GetParentsList()
            return render_template('viewtable.html',headings=headings,data=data)
    


if __name__ == "__main__":
    app.run(debug=True)