from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length,Regexp,Email


class LoginForm(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),Length(min=6,max=16)])
    

class SignupForm(FlaskForm):
    username = StringField('username', validators=[Required(), Length(1, 100), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('uassword', validators=[
        DataRequired(),
        Length((8,16), message='Password must be between 8 to 16 characters long'),
        Regexp(r'[A-Z]', message='Password must contain at least one uppercase letter'),
        Regexp(r'[a-z]', message='Password must contain at least one lowercase letter'),
        Regexp(r'[0-9]', message='Password must contain at least one digit'),
        Regexp(r'[@$!%*?&]', message='Password must contain at least one special character (@, $, !, %, *, ?, &)'),
    ])
    email = StringField('email', validators=[
        DataRequired(),
        Email(message='Invalid email address')
    ])
    phno= StringField('phno',validators=[
        DataRequired(),
        Length(10)
    ])
    address= StringField('address',validators=[
        DataRequired(),
        Length(5,100)
    ])

    age = IntegerField('Age', validators=[
        DataRequired(), 
        NumberRange(min=10, max=100, message="You must be between 10 and 100 years old.")])


    

