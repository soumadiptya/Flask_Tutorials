# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 22:35:53 2019

@author: souma
"""

#%% Import libraries
from flask import Flask

#%% Instantiate an app
app = Flask(__name__)

#%% App Layout
@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

#%% Run app
if __name__ == '__main__':
    app.run(debug=True)