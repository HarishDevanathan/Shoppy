from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,SelectField
from wtforms.validators import DataRequired,Length,Regexp,Email,NumberRange


class LoginForm(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),Length(min=6,max=16)])
    

class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 100), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')])
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

    countrycode = SelectField('countrycode', choices=[+93, +355, +213, +1684, +376, +244, +1264, +672, +1268, +54, +374, +297, +61, +43, +994, +1242, +973, +880, +1246, +375, +32, +501, +229, +1441, +975, +591, +387, +267, +55, +246, +1284, +673, +359, +226, +257, +855, +237, +1, +238, +345, +236, +235, +56, +86, +61, +61, +57, +269, +242, +243, +682, +506, +225, +385, +53, +357, +420, +45, +253, +1, +1, +593, +20, +503, +240, +291, +372, +251, +500, +298, +679, +358, +33, +594, +689, +241, +220, +995, +49, +233, +350, +30, +299, +1473, +502, +44, +224, +245, +595, +509, +504, +852, +36, +354, +91, +62, +98, +964, +353, +44, +972, +39, +1, +81, +44, +962, +7, +254, +686, +965, +996, +856, +371, +961, +266, +231, +218, +423, +370, +352, +853, +389, +261, +265, +60, +960, +223, +356, +691, +596, +222, +230, +262, +52, +691, +373, +377, +976, +382], default='+91', validators=[DataRequired()])
    
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


    

