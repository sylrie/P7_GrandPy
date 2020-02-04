#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, jsonify 
from search import UserRequest

app = Flask(__name__)

@app.route('/grandpy/<question>/')
def grandpy(question):
    
    data = UserRequest(question)
    return data.response

@app.route('/')
def index():
    """ home page"""
    return render_template("home.html")

if __name__ == "__main__":
    app.run()