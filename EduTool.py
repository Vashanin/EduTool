# !/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request, url_for, redirect
import traceback
from Model.User import *

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template("home.html")
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
                INFO = "Welcome!"
            else:
                ERROR = "Oops. You enter wrong auth data."

        return render_template("login.html", INFO=INFO, ERROR=ERROR)
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()


@app.route('/sign_up/')
def signup():
    try:
        return render_template("signup.html", INFO=None)
    except Exception as e:
        traceback.format_exc()

@app.route("/new_user/", methods=["POST"])
def new_user():
    try:
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            name = request.form["name"]
            surname = request.form["surname"]

            user = User(email, password, name, surname)
            User.add_user(user, "teacher")

        return render_template("signup.html", INFO="Your account has been succesfully created!")
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()


if __name__ == '__main__':
    app.run()