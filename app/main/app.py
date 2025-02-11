from flask import Flask, render_template, redirect, url_for, session, flash, request
from forms import LoginForm, SignupForm, ProfileForm, ForgotPasswordForm, OTPForm
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
from sqlalchemy import func,desc
import random
import json
import time
from datetime import datetime
import threading

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

@app.route('/clear-session', methods=['POST'])
def clear_session():
    session.clear()
    return redirect(url_for('login'))

@app.route('/aboutus')
def aboutus():
    if 'user_id' not in session:
        flash("Log in first","warning")
        return redirect(url_for('login'))
    return render_template('aboutuspage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors={}
    errors['username']=""
    errors['password']=""

    def userclear():
        errors['username']=""
    def passclear():
        errors['password']=""
    
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
                errors['password']="Invalid password"
                errors['username']=""
                #time.sleep(2)
                #errors['password']=""
        else:
            errors['password']=""
            errors['username']="Invalid username"
            #time.sleep(2)
            #errors['username']=""
    return render_template("loginpage.html", form=form,errors=errors)

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

@app.route('/home',methods=['GET','POST'])
def home():
    if 'username' not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for('login'))
    
    check_user=user_data.query.filter(func.lower(user_data.username)==session.get('username').lower()).first()
    print(check_user.username)

    if request.method=='POST':
        tempstr=request.form.get('searchbar')
        if(tempstr!=""):
            return redirect(url_for('search',prod=tempstr))
        else:
            return redirect(url_for('home'))
    if check_user:
        print("not null")
        if check_user.hist:
            userhistory=check_user.hist
            print(userhistory)
            print(type(userhistory[0]))
            productsarr=set()
            for i in userhistory:
                print(i)
                temp = products.query.filter(func.lower(products.name).contains(i.lower())).all()
                for j in temp:
                    productsarr.add(j)
                temp = products.query.filter(func.lower(products.brand).contains(i.lower())).all()
                for j in temp:
                    productsarr.add(j)
            print(productsarr)
            return render_template("homepage.html",productsarr=productsarr)
        
    else:
        productsarr=[]
        print(productsarr)
        return render_template("homepage.html",productsarr=productsarr)
'''
@app.route('/home')
def home():
    if 'username' not in session:
        flash("Please log in first.", "warning")
        return redirect(url_for('login'))
    
    
    check_product=products.query.filter_by(name="water bottle")
    print(check_product)
    username = session['username']
    return render_template("homepage.html",productsarr=check_product)
'''
    
def generate_id():
    with app.app_context():
        id = user_data.generate_uid()
    return id

@app.route('/profileedit', methods=['GET', 'POST'])
def profile():
    if 'username' in session:
        username = session['username']
        user = user_data.query.filter_by(username=username).first()

        if user:
            form = ProfileForm()

            form.username.data = user.username
            form.passw.data = '**********'  
            form.email.data = user.email
            phno= user.phno
            form.phno.data=phno[3:]
            form.address.data=user.address
            countrycode=phno[:3]

            if request.method == 'POST':
                form1 = ProfileForm()
                new_email = form1.email.data.strip().lower() if form1.email.data else form.email.data
                new_phno= form1.phno.data if form1.phno.data else form.phno.data
                new_address= form1.address.data if form1.address.data else form.address.data
                existing_user = user_data.query.filter_by(email=new_email).first()
                existing_phno = user_data.query.filter_by(phno=new_phno).first()

                if existing_user and existing_user.username != user.username:
                    flash('This email is already taken by another user.', 'danger')
               
                elif '.' not in new_email or '@' not in new_email:
                    flash('Invalid email format.', 'danger')
                
                if existing_phno and existing_phno.username != user.username:
                    flash('This email is already taken by another user.', 'danger')
               
                if new_phno and (len(new_phno) != 10 or not new_phno.isdigit()):
                    flash('Phone number must consist of exactly 10 digits and only numbers.', 'danger')
                    return render_template('profile.html', user=user, form=form)
                elif len(new_address)<5:
                     flash('Invalid address format.', 'danger')
                else:
                    user.email = new_email
                    user.phno = countrycode+new_phno
                    user.address=new_address
                    db.session.commit()
                    flash('Email updated successfully!', 'success')

                return redirect(url_for('profile'))
                
            else:
                flash('Invalid email format.', 'danger')

            return render_template('profile.html', user=user, form=form)

        else:
            return 'User not found'

    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    
    flash('You have been logged out successfully!', 'success')
    return redirect(url_for('login'))

    
def genotp():
    return random.randint(100000,999999)

@app.route('/forgotpassword',methods=['GET','POST'])
def forgotpassword():
    form=ForgotPasswordForm()
    error_messages={}
    if form.validate_on_submit():
        session['username']=form.username.data
        session['email']=form.email.data
        print(form.username.data)
        print(form.email.data)
        if checkEmail(session.get('username'),session.get('email'))==1:
            session['otptemp']=str(genotp())
            send_email( session.get('otptemp') ,[ session.get('email')] )
            session['switch']=1
            return redirect(url_for('forgverification'))
        elif checkEmail(session.get('username'), session.get('email'))==0:
            error_messages['email']='*Invalid email*'
            error_messages['username']=''
        elif checkEmail(session.get('username'), session.get('email'))==-1:
            error_messages['username']='*Invalid username*'
            error_messages['email']=''
    return render_template('forgotpassword.html',form=form,errors=error_messages)


def checkEmail(username,checkmail) -> int:
    with app.app_context():
        check_user = user_data.query.filter(func.lower(user_data.username) == username.lower()).first()
        if check_user:
            if check_user.email==checkmail:
                return 1
            else:
                return 0
        else:
            return -1
        
@app.route('/forgotpassword/verfication',methods=['GET','POST'])
def forgverification():
    if 'switch' in session:
        form=OTPForm()
        if session.get('switch')==1:
            if form.validate_on_submit():
                otp=form.otp.data
                if(session.get('otptemp')==otp):
                    username=session.get('username')
                    session.clear()
                    session['username']=username
                    return redirect(url_for('login'))
            return render_template('enterotp.html',form=form)
        else:
            flash('enter username and email first','Warning')
            return redirect(url_for('forgotpassword'))
    else:
        flash('enter username and email first','Warning')
        return redirect(url_for('forgotpassword'))

@app.route('/clearsession',methods=['GET'])
def clearsession():
    session.clear()
    return redirect(url_for('login'))



@app.route('/product/<productid>')
def product(productid):
    product = products.query.filter(products.product_id == productid ).first()
    
    if product:
        comments =product.comments
        
        for comment in comments:
            comment_date_str = comment.get("date")
            if comment_date_str:
                comment_date = datetime.strptime(comment_date_str, "%Y-%m-%d")
                days_ago = (datetime.now() - comment_date).days
                if(days_ago>=365):
                    years=days_ago//365.25
                    if(years>1):
                        comment["days_ago"]=f"{int(years)} years ago"
                    else:
                        comment["days_ago"]="1 year ago"
                elif days_ago>=31:
                    months=days_ago//30
                    if(months>1):
                        comment["days_ago"]=f"{int(months)} months ago"
                    else:
                        comment["days_ago"]="1 month ago"
                else:
                    comment["days_ago"] = f"{days_ago} days ago" if days_ago > 0 else "JUST NOW"
            else:
                comment["days_ago"] = "Date not available"


        return render_template('productvisit.html', product=product, comments=comments)

    return "Product not found"


@app.route('/profback')
def profilemod():
    if 'username' not in session:
        flash('login first','warning')
        return redirect(url_for('login'))
    brand_dict={} 
    user=user_data.query.filter(func.lower(user_data.username)==session.get('username').lower()).first()
    for i in user.owned_products:
        tempprod=products.query.filter(products.product_id==i).first()
        if tempprod:
            if tempprod.brand in brand_dict:
                brand_dict[tempprod.brand]+=1
            else:
                brand_dict[tempprod.brand]=1
    tempkey=""
    tempvalue=-1
    for key,value in brand_dict.items():
        if(value>tempvalue):
            tempkey=key
            tempvalue=value
    print(user.gender)
    if tempkey=="":
        tempkey='-'
    
    return render_template('profilemod.html',user=user,msb=tempkey)

@app.route('/search/<prod>',methods=['GET','POST'])
def search(prod):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method=='POST':
        tempstr=request.form.get('searchbar')
        if(tempstr!=""):
            return redirect(url_for('search',prod=tempstr))
        else:
            return redirect(url_for('home'))

    searched=[]
    temp=products.query.filter(products.product_id==prod).first()
    if(temp):
            searched.append(temp)
    temp=products.query.filter(func.lower(products.name).contains(prod.lower()) & (products.stock > 0)).order_by(desc(products.units_sold))
    templ=[]
    mostsold=""
    for i in temp:
            templ.append(i)
            searched.append(i)
    if templ!=[] :
        mostsold=templ[0].product_id
        
    return render_template('search.html',searched=searched,mostsold=mostsold)
    
if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5001/login")
    app.run(debug=True, port=5001)
