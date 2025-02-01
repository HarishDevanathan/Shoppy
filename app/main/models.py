from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import random
from datetime import date
db=SQLAlchemy()

class user_data(db.Model):
    __tablename___="user_data"
    username=db.Column(db.String(100),primary_key=True)
    passw=db.Column(db.String(500))
    email=db.Column(db.String(100))
    phno=db.Column(db.String(15))
    address=db.Column(db.String(100),unique=True)
    doj=db.Column(db.Date)
    id=db.Column(db.String(11),nullable=False,unique=True)
    cart=db.Column(db.JSON)
    orders=db.Column(db.JSON)
    wallet=db.Column(db.Integer)
    owned_products=db.Column(db.JSON)
    hist=db.Column(db.JSON)
    wishlist=db.Column(db.JSON)
    gender=db.Column(db.String(1))
    def __repr__(self):
        return f'{self.username}'
    
    @staticmethod
    def generate_uid():
        random_number=random.randint(10000000,99999999)
        while(True):
            cust='01-'+str(random_number)
            sel='02-'+str(random_number)
            check_user=user_data.query.filter(or_(user_data.id==cust,user_data.id==sel)).first()
            if(not check_user):
                return cust
            random_number=random.randint(10000000,99999999)

class products(db.Model):
    __tablename__="products"
    name=db.Column(db.String(100))
    brand=db.Column(db.String(100))
    product_id=db.Column(db.String(16),primary_key=True)
    id=db.Column(db.String(11),db.ForeignKey('user_data.id'),nullable=False)
    discountpercentage=db.Column(db.Integer)
    discountprice=db.Column(db.Integer)
    imagepath=db.Column(db.String(200))
    productdesc=db.Column(db.String(500))
    rating=db.Column(db.Float)
    stock=db.Column(db.Integer)
    units_sold=db.Column(db.Integer)
    rating_count=db.Column(db.Integer)
    smdesc=db.Column(db.String(100))
    mrp=db.Column(db.Integer)
    comments=db.Column(db.JSON)
    user=db.relationship('user_data',backref='products')

    def __repr__(self):
        return f'{self.product_id}'



    



            


