from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,SelectField,SubmitField,RadioField
from wtforms.validators import DataRequired,Length,Regexp,Email,NumberRange
from models import db, user_data

class LoginForm(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired(),Length(min=6,max=16)])
    
class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 100), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots, or underscores')])
    
    password = PasswordField('password', validators=[
        DataRequired()
    ])
    
    email = StringField('email', validators=[
        DataRequired(),
        Email(message='Invalid email address')
    ])
    
    countrycode = SelectField('countrycode', 
        choices=[
            ('+93', '+93'),
            ('+355', '+355'),
            ('+213', '+213'),
            ('+1684', '+1684'),
            ('+376', '+376'),
            ('+244', '+244'),
            ('+1264', '+1264'),
            ('+672', '+672'),
            ('+1268', '+1268'),
            ('+54', '+54'),
            ('+374', '+374'),
            ('+297', '+297'),
            ('+61', '+61'),
            ('+43', '+43'),
            ('+994', '+994'),
            ('+1242', '+1242'),
            ('+973', '+973'),
            ('+880', '+880'),
            ('+1246', '+1246'),
            ('+375', '+375'),
            ('+32', '+32'),
            ('+501', '+501'),
            ('+229', '+229'),
            ('+1441', '+1441'),
            ('+975', '+975'),
            ('+591', '+591'),
            ('+387', '+387'),
            ('+267', '+267'),
            ('+55', '+55'),
            ('+246', '+246'),
            ('+1284', '+1284'),
            ('+673', '+673'),
            ('+359', '+359'),
            ('+226', '+226'),
            ('+257', '+257'),
            ('+855', '+855'),
            ('+237', '+237'),
            ('+1', '+1'),
            ('+238', '+238'),
            ('+345', '+345'),
            ('+236', '+236'),
            ('+235', '+235'),
            ('+56', '+56'),
            ('+86', '+86'),
            ('+61', '+61'),
            ('+57', '+57'),
            ('+269', '+269'),
            ('+242', '+242'),
            ('+243', '+243'),
            ('+682', '+682'),
            ('+506', '+506'),
            ('+225', '+225'),
            ('+385', '+385'),
            ('+53', '+53'),
            ('+357', '+357'),
            ('+420', '+420'),
            ('+45', '+45'),
            ('+253', '+253'),
            ('+1', '+1'),
            ('+1', '+1'),
            ('+593', '+593'),
            ('+20', '+20'),
            ('+503', '+503'),
            ('+240', '+240'),
            ('+291', '+291'),
            ('+372', '+372'),
            ('+251', '+251'),
            ('+500', '+500'),
            ('+298', '+298'),
            ('+679', '+679'),
            ('+358', '+358'),
            ('+33', '+33'),
            ('+594', '+594'),
            ('+689', '+689'),
            ('+241', '+241'),
            ('+220', '+220'),
            ('+995', '+995'),
            ('+49', '+49'),
            ('+233', '+233'),
            ('+350', '+350'),
            ('+30', '+30'),
            ('+299', '+299'),
            ('+1473', '+1473'),
            ('+502', '+502'),
            ('+44', '+44'),
            ('+224', '+224'),
            ('+245', '+245'),
            ('+595', '+595'),
            ('+509', '+509'),
            ('+504', '+504'),
            ('+852', '+852'),
            ('+36', '+36'),
            ('+354', '+354'),
            ('+91', '+91'),
            ('+62', '+62'),
            ('+98', '+98'),
            ('+964', '+964'),
            ('+353', '+353'),
            ('+44', '+44'),
            ('+972', '+972'),
            ('+39', '+39'),
            ('+1', '+1'),
            ('+81', '+81'),
            ('+44', '+44'),
            ('+962', '+962'),
            ('+7', '+7'),
            ('+254', '+254'),
            ('+686', '+686'),
            ('+965', '+965'),
            ('+996', '+996'),
            ('+856', '+856'),
            ('+371', '+371'),
            ('+961', '+961'),
            ('+266', '+266'),
            ('+231', '+231'),
            ('+218', '+218'),
            ('+423', '+423'),
            ('+370', '+370'),
            ('+352', '+352'),
            ('+853', '+853'),
            ('+389', '+389'),
            ('+261', '+261'),
            ('+265', '+265'),
            ('+60', '+60'),
            ('+960', '+960'),
            ('+223', '+223'),
            ('+356', '+356'),
            ('+691', '+691'),
            ('+596', '+596'),
            ('+222', '+222'),
            ('+230', '+230'),
            ('+262', '+262'),
            ('+52', '+52'),
            ('+691', '+691'),
            ('+373', '+373'),
            ('+377', '+377'),
            ('+976', '+976'),
            ('+382', '+382')
        ],
        default='+91',
        validators=[DataRequired()]
    )
    
    gender = RadioField('gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()],render_kw={'class':'no_bullets'})

    phno = StringField('phno', validators=[
        DataRequired(),
        Length(10)
    ])
    
    address = StringField('address', validators=[
        DataRequired(),
        Length(5, 100)
    ])

class ProfileForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    passw = StringField('passw',validators=[DataRequired()])
    email = StringField('email', validators=[
        DataRequired(),
        Email(message='Invalid email address')
    ])
    phno = StringField('phno', validators=[
        DataRequired(),
        Length(10)
    ])
    countrycode = StringField('countrycode', validators=[
        DataRequired(),
        Length(3)
    ])
    address = StringField('address', validators=[
        DataRequired(),
        Length(5, 100)
    ])
    submit = SubmitField('Save')

class ForgotPasswordForm(FlaskForm):
    username=StringField('username',validators=[DataRequired()])
    email=StringField('email', validators=[DataRequired(),Email(message='Invalid mail address')])

class OTPForm(FlaskForm):
    otp=StringField('otp',validators=[DataRequired(),Length(6,6)],render_kw={"placeholder":"Enter the 6 digit OTP"})
    
    
    

    

