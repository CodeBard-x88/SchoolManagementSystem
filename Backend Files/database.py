from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ssms'


try:
    # Attempt to create the SQLAlchemy object and bind it to the app
    db = SQLAlchemy(app)
    print ('database connected')
except Exception as e:
    print(f"Error creating SQLAlchemy object: {e}")
    db = None

@app.route('/')
def hello_world():
    return render_template("login.html")

if(__name__ == "__main__"):
    app.run(debug=True)