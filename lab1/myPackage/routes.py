from flask import render_template, url_for, redirect, flash
from myPackage.__init__ import db, app
from myPackage.forms import RegistrationForm, LoginForm
from myPackage.models import Student
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required

# --------------------------- routes ---------------------------
# Decorator add functionality to functions without adding code
# (.route) Decorator handles all the complicated backend stuff
# to allow us to have a function for this specific route


nav = [
    {
        'function': 'home',
        'url': 'home',
    },
    {
        'function': 'about',
        'url': 'about',
    },
    {
        'function': 'redirectFunc',
        'url': 'redirect',
    }
]


# Homepage Endpoint
@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', navs=nav, title="home page")

# About Endpoint


@app.route('/about')
def about():
    return render_template('about.html', navs=nav, title='about page')

# Redirect Endpoint


@app.route('/redirect')
def redirectFunc():
    return redirect(url_for('home'))


bcrypt = Bcrypt()


@app.route('/register', methods=['GET', 'POST'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        with app.app_context():
            # to make hash for any password pefor savring it in database we should
            # [1] install flask-bcrypt ==>pip install flask-bcrypt
            # [2] from flask-bcrypt import Bcrypt

            hashed_password = bcrypt.generate_password_hash(
                form.password.data).decode('utf8')
            student = Student(username=form.username.data,
                              email=form.email.data, password=hashed_password)
            db.session.add(student)
            db.session.commit()
        flash(f"Registration Successfull {form.username.data}", "success")
        return redirect(url_for('login'))

    return render_template('register.html', navs=nav, title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            username_1 = form.username.data
            with app.app_context():
                student = Student.query.filter_by(username=username_1).first()
            if student and bcrypt.check_password_hash(student.password, form.password.data):
                login_user(student)
                flash(f"Login Successfull {username_1}", "success")
                return redirect(url_for('home'))

        return render_template('login.html', navs=nav, title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Redirect Endpoint
# @app.route('/test')
# def test():
# 	result = [
# 	{
# 		'name': 'About page',
# 		'url': "about"
# 	},
# 	{
# 		'name': 'Home page',
# 		'url': "home"
# 	},
# 	]
# 	return render_template('test.html', result=result)


# result = [
# 	{
# 		'student': 'yahia',
# 		'grade': 10,
# 		'year': 2021
# 	},
# 	{
# 		'student': 'ahmed',
# 		'grade': 20,
# 		'year': 2020
# 	},
# 	{
# 		'student': 'osama',
# 		'grade': 30,
# 		'year': 2019
# 	}
# 	]
