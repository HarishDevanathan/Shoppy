from flask import Flask, render_template, redirect, url_for
from forms import LoginForm,SignupForm
from werkzeug.security import generate_password_hash, check_password_hash
from models import user_data,db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SECRET_KEY'] = "This_is_a_secret_key_@123!@#"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:ganesh2005*@localhost/project_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutuspage.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        check_user = user_data.query.filter_by(username=username).first()
        if check_user:
            if check_password_hash(check_user.passw, password):
                form.username.data=''
                form.password.data=''
                return redirect(url_for('welcome', username=username))
            else:
                return 'Invalid credentials'
        else:
            return "Username doesn't exist"
    return render_template("loginpage.html", form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        phno = form.phno.data
        address = form.address.data
        age= form.age.data
        uid=generate_uid()
        check_uid=user_data.query.filter_by(uid=uid).first()
        while check_uid:
            uid=generate_uid()
            check_uid=user_data.query.filter_by(uid=uid).first()
        
        check_username = user_data.query.filter_by(username=username).first()
        check_phno=user_data.query.filter_by(phno=phno).first()
        
        if check_username:
            return 'Username already taken'
            if check_phno:
                return 'Phone number already exist'
            else:
                hashed_password = generate_password_hash(password)
                new_user = user_data(username=username,password=hashed_password,email=email,phno=phno,address=address,age=age,id=uid,cart=[],orders=[], wallet=0,products=[],hist=[])
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('welcome', username=username))

    return render_template("signup.html")

@app.route('/home/<username>')
def welcome(username):
    return render_template('homepage.html',username=username)


@app.route('/generate_uid',methods=['GET'])
def generate_uid():
    with app.app_context():
        id=user_data.generate_uid()
    return id

if __name__ == "__main__":
    app.run(debug=True,port=5000)
