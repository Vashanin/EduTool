# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Exceptions.UserIsAlreadyExistException import *
from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask_session import Session
import traceback
from Model.User import *

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
                User.add_user(user, "teacher")
                INFO = "You account has been succesfully created."
            except UserIsAlreadyExistException as e:
                ERROR = e.getInfo()

        return render_template("signup.html", INFO=INFO, ERROR=ERROR)
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()

@app.route("/personal_page/")
def personal_page():
    try:
        USER = User.getUserByEmail(session["current_user"])

        return render_template("personal_page.html", USER=USER)
    except Exception as e:
        print("Trougles with personal_page method: " + str(e.args))
        traceback.format_exc()

if __name__ == '__main__':
    app.run()