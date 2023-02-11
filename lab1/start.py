# import flask
from flask import Flask, render_template, url_for, redirect, flash
import os

# create flask app, __name__ = tell flask where to look
app = Flask(__name__)

# Add this secret key when you create database and forms
# Get Random letters from python terminal
# import secrets -> secrets.token_hex(16)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

# FLASK_APP= 'start.py'
# DEBUG = 1
# SECRET_KEY = "b'_5#y2L"F4Q8z\n\xec]/"
# --------------------------- routes ---------------------------
# Decorator add functionality to functions without adding code
# (.route) Decorator handles all the complicated backend stuff
# to allow us to have a function for this specific route


nav= [
	{
		'function': 'home',
		'url':'home',
	},
	{
		'function': 'about',
		'url':'about',
	},
	{
		'function': 'redirectFunc',
		'url':'redirect',
	}
]


# Homepage Endpoint
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title="home page",nav=nav)



# About Endpoint
@app.route('/about')
def about():
	return render_template('about.html', title='about page',nav=nav)

# Redirect Endpoint
@app.route('/redirect')
def redirectFunc():
	return redirect(url_for('home'),nav=nav)



# result = [
# {
# 	'student': 'yahia',
# 	'grade': 10,
# 	'year': 2021
# },
# {
# 	'student': 'ahmed',
# 	'grade': 20,
# 	'year': 2020
# },
# {
# 	'student': 'osama',
# 	'grade': 30,
# 	'year': 2019
# }
# ]
# user = "asd"
# usernames = ["ahmed","mahmoud","mohammed"]
# if user in usernames:
# 	flash(f"Login Successful : {user}", "success")
# 	return render_template('home.html', result=result, title="home page")
# else:
# 	flash(f"Login Unsuccessful : {user}", "danger")
# 	# return redirect(url_for('about'))
# 	return render_template('about.html')

# About Endpoint
# @app.route('/about')
# def about():
# 	return render_template('about.html', title='about page')

# # Redirect Endpoint
# @app.route('/redirect')
# def redirectFunc():
# 	return redirect(url_for('home'))
if __name__ == '__main__':
	app.run(debug=True)