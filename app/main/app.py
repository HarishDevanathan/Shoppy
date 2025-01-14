import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask,render_template,redirect,url_for
from forms import LoginForm
from werkzeug.security import generate_password_hash,check_password_hash
from models import user
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__ , template_folder="../templates", static_folder="../static")
app.config['SECRET_KEY']="This_is_a_secret_key_@123!@#"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:ganesh2005*@localhost/dummy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutuspage.html")

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        
        check_user=user.query.filter_by(username=username).first()
        if( check_user):
            if(check_user.password==password):
                return redirect(url_for('welcome',username=username))
            else:
                return 'invalid credentials'
        else:
            return "username does'nt exists"
    return render_template("loginpage.html",form=form)

@app.route('/welcome/<username>')
def welcome(username):
    return f'Welcome {username}'


if(__name__=="__main__"):
    app.run(debug=True,port=5001)

