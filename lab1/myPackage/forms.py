# pip install flask-wtf
# pip install email_validator

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from myPackage.models import Student


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, max=20)
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField(
        'Sign Up'
    )
    # validation if user name is dublicate

    def validate_username(self, username):
        student = Student.query.filter_by(username=username.data)
        if student:
            raise ValidationError("user name is exsits")

    # validation if user name is dublicate
    def validate_email(self, email):
        student = Student.query.filter_by(email=email.data)
        if student:
            raise ValidationError("user email is exsits")

    def validate(self, extra_validators=None):
        return super().validate(extra_validators)

    def validate_on_submit(self, extra_validators=None):
        return super().validate_on_submit(extra_validators)


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, max=20)
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField(
        'Sign Up'
    )
