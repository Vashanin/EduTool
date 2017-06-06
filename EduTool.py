# !/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request, url_for, redirect
import traceback

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
        return render_template("login.html")
    except Exception as e:
        traceback.format_exc()

@app.route("/user_auth/", methods=["POST"])
def user_auth():
    try:
        if request.method == "POST":
            user_email = request.form["user_email"]
            user_password = request.form["user_password"]

        return redirect(url_for("login"))
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()


@app.route('/signup/')
def signup():
    try:
        return render_template("signup.html")
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

        return redirect(url_for("signup"))
    except Exception as e:
        print("Exception has been caught: " + e.args[0])
        traceback.format_exc()


if __name__ == '__main__':
    app.run()