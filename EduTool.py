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

if __name__ == '__main__':
    app.run()