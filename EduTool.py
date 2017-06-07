    # !/usr/bin/env python
# -*- coding: utf-8 -*-

from Exceptions.UserIsAlreadyExistException import *
from Exceptions.SubjectIsAlreadyExistException import *
from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask_session import Session
import traceback
from Model.User import *
from Model.Subject import *

app = Flask(__name__)
app.secret_key = 'ilovematanverymuch'

@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        traceback.format_exc()

@app.route('/log_out/')
def logout():
    try:
        session["current_user"] = None
        return render_template("index.html")
    except Exception as e:
        traceback.format_exc()

@app.route('/login/')
def login():
    try:
        return render_template("login.html", INFO=None, ERROR=None)
    except Exception as e:
        traceback.format_exc()

@app.route("/user_auth/", methods=["POST"])
def user_auth():
    try:
        INFO = None
        ERROR = None

        if request.method == "POST":
            user_email = request.form["user_email"]
            user_password = request.form["user_password"]

            if User.authenticate(user_email, user_password):
                session["current_user"] = user_email
                INFO = "Welcome! "
            else:
                ERROR = "Oops. You enter wrong auth data."

        return render_template("login.html", INFO=INFO, ERROR=ERROR)
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()

@app.route('/sign_up/')
def signup():
    try:
        return render_template("signup.html", INFO=None, ERROR=None)
    except Exception as e:
        traceback.format_exc()

@app.route("/new_user/", methods=["POST"])
def new_user():
    try:
        INFO = None
        ERROR = None

        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            name = request.form["name"]
            surname = request.form["surname"]

            user = User(email, password, name, surname)
            try:
                user.add_user("teacher")
                INFO = "You account has been succesfully created."
            except UserIsAlreadyExistException as e:
                ERROR = e.getInfo()

        return render_template("signup.html", INFO=INFO, ERROR=ERROR)
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()

@app.route("/user_courses/")
def user_courses():
    try:
        teacher = User.getUserByEmail(session["current_user"])

        print(teacher)
        print(Subject.getAllSubjectsOfTeacher(teacher))

        return render_template("user_courses.html", SUBJECTS=Subject.getAllSubjectsOfTeacher(teacher))
    except Exception as e:
        print("Troubles with user_courses method: " + str(e.args))
        traceback.format_exc()

@app.route("/all_courses/")
def all_courses():
    try:
        return render_template("all_courses.html", SUBJECTS=Subject.getAllSubjects())
    except Exception as e:
        print("Troubles with all_courses method: " + str(e.args))
        traceback.format_exc()

@app.route("/add_new_course/")
def add_new_course():
    try:
        return render_template("add_new_course.html", ERROR=None, INFO=None)
    except Exception as e:
        print("Troubles with adding new course")
        traceback.format_exc()

@app.route("/add_new_course_handler/", methods=["POST", "GET"])
def add_new_course_handler():
    try:
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            image_url = request.form["image_url"]

            teacher = User.getUserByEmail(session["current_user"])
            subject = Subject(title, description, image_url, teacher)

            ERROR = None
            INFO = None

            try:
                subject.add_subject()
                INFO = "New subject has been succesfully added"
            except SubjectIsAlreadyExistException as e:
                ERROR = "Subject with this title has been already created"

            return render_template("add_new_course.html", ERROR=ERROR, INFO=INFO)
    except Exception as e:
        print("Troubles with adding new course")
        traceback.format_exc()

@app.route("/personal_page/")
def personal_page():
    try:
        USER = User.getUserByEmail(session["current_user"])
        return render_template("personal_page.html", USER=USER, CHANGE=False)
    except Exception as e:
        print("Troubles with EduTool.personal_page: " + str(e.args))

if __name__ == '__main__':
    app.run()