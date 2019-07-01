# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 22:35:53 2019

@author: souma
"""

#%% Import libraries
from flask import Flask
from flask import render_template

#%% Instantiate an app
app = Flask(__name__)

#%% Add data
posts = [ 
        {'author':'Soumadiptya Chakraborty',
        'title':'Flask app with Layout',
        'content':'No content... YET',
        'date_posted':'July 1st 2019'
        },
        {'author':'Sara Jane Chakraborty',
        'title':'My daughter',
        'content':'No content... YET',
        'date_posted':'July 2nd 2024'
        }
]


#%% App Layout
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
#%% Run app
if __name__ == '__main__':
    app.run(debug=True)