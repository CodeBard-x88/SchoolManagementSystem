from flask import Flask, render_template, request, redirect
from database import db
from Users import Users

class Admin(Users):

    def __init__(self,name,username,password,email,phone):
        super.__init__(name,username,password,email,phone)

    def Login(self):
        return super().Login()