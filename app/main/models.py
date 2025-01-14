from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class user_data(db.Model):
    __tablename___="user_data"
    username=db.Column(db.String(100),primary_key=True)
    passw=db.Column(db.String(500))
    email=db.Column(db.String(100))
    phno=db.Column(db.String(15))
    address=db.Column(db.String(100),unique=True)
    doj=db.Column(db.Date)
    age=db.Column(db.Integer)
    id=db.Column(db.String(11),nullable=False,unique=True)
    cart=db.Column(db.JSON)
    orders=db.Column(db.JSON)
    wallet=db.Column(db.Integer)
    products=db.Column(db.JSON)
    hist=db.Column(db.JSON)

    def __repr__(self):
        return f'{self.username}'