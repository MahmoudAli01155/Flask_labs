# flask imports





from sqlalchemy import MetaData
from flask import Flask
import os
# DB Imports
from flask_sqlalchemy import SQLAlchemy


# install flask migrate ==>pip install flask-migrate
# import flask-migrate package
from flask_migrate import Migrate

# install log in manger ==>pip install flask-login
# import flask login manger
from flask_login import LoginManager


# create flask app, __name__ = tell flask where to look
app = Flask(__name__)

# Add this secret key when you create database and forms
# Get Random letters from python terminal
# import secrets -> secrets.token_hex(16)
app.config['SECRET_KEY'] = '92bb1cc78650ae59ae9b8266bac43d93'

# db configs , /// = current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskProject.db'


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(app, metadata=MetaData(naming_convention=convention))

# db = SQLAlchemy(app)

# flask-migrations shoud fild with the models that you want to make for them migrations
# so we will import models flile befor create migration object


# make migrate objecte
migrate = Migrate(app, db, render_as_batch=True)
# to init file migrate file you should run command ==> flask db init ==>once in the project
# every time you need to make migration to sum changes in the models file
# you shoud run command ==> flask db migrate -m 'write any comente hier'
# to commit the changes in migrate folder in database
# you shoud run command ==> flask db upgrade

# useing log in manger system or packge

login_manager = LoginManager(app)


from myPackage.routes import *
from .models import *

