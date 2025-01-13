from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates')


# Configuration for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Harish123@localhost/project_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a Model for your data
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    users = UserData.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    new_user = UserData(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
