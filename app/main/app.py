from flask import Flask, render_template, redirect, url_for, session, flash, request
from forms import LoginForm, SignupForm,ProfileForm
from werkzeug.security import generate_password_hash, check_password_hash
from models import user_data,db
from flask_sqlalchemy import SQLAlchemy
from mails import send_email,init_mail
from flask import Flask, render_template, redirect, url_for
from datetime import date
from models import user_data,products, db
from mails import send_email, init_mail
from datetime import timedelta
import webbrowser
from sqlalchemy import func


app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SECRET_KEY'] = "This_is_a_secret_key_@123!@#"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:ganesh2005*@localhost/project_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'shoppysemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'tazd must smqk wxaw'
app.config['MAIL_DEFAULT_SENDER'] = 'shoppysemail@gmail.com'
app.permanent_session_lifetime=timedelta(hours=2)

db.init_app(app)
init_mail(app)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/clear-session', methods=['POST'])
def clear_session():
    session.clear()
    return '', 200

@app.route('/aboutus')
def aboutus():
    if 'user_id' not in session:
        flash("Log in first","warning")
        return redirect(url_for('login'))
    return render_template('aboutuspage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        check_user = user_data.query.filter(func.lower(user_data.username)==username.lower()).first()
        if check_user:
            if check_password_hash(check_user.passw, password):
                session['username'] = check_user.username
                session['user_id'] = check_user.id
                flash("Login successful!", "success")
                return redirect(url_for('home'))
            else:
                flash("Invalid credentials.", "danger")
        else:
            flash("Username doesn't exist.", "danger")
    return render_template("loginpage.html", form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        phno = form.phno.data
        countrycode = form.countrycode.data
        address = form.address.data
        uid = generate_id()
        full_phno = countrycode + phno

        check_username = user_data.query.filter_by(username=username).first()
        check_phno = user_data.query.filter_by(phno=full_phno).first()

        if check_username:
            flash("Username already taken.", "warning")
            return redirect(url_for('signup'))
        if check_phno:
            flash("Phone number already exists.", "warning")
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)
        new_user = user_data(
            username=username,
            passw=hashed_password,
            email=email,
            phno=full_phno,
            address=address,
            doj=date.today(),
            id=uid,
            cart=[],
            orders=[],
            wallet=0,
            owned_products=[],
            hist=[]
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Signup successful! Please log in.", "success")
        return redirect(url_for('login'))
    else:
        print(form.errors) 
    return render_template("signup.html", form=form)


@app.route('/home')
def home():
    if 'user_id' not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for('login'))
    
    check_product=products.query.filter_by(name="water bottle")
    print(check_product)
    username = session['username']
    return render_template("homepage.html",productsarr=check_product)

def generate_id():
    with app.app_context():
        id = user_data.generate_uid()
    return id

@app.route('/send-email')
def send_email_route():
    send_email('This is a test mail', ['ganeshkumar78602005@gmail.com', 'harishdevanathan123@gmail.com'])
    return 'Email Sent'

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        user = user_data.query.get(username)
        
        if user:
            form=ProfileForm()
            form.username.data = session['username']
            return render_template('profile.html', user=user,form=form)
        else:
            return 'User not found'
    else:
        return redirect(url_for('login'))
    
if __name__ == "__main__":
    #webbrowser.open("http://127.0.0.1:5001/login")
    app.run(debug=True, port=5001)
