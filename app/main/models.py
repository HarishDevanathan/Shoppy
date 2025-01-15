from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import random
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

    



            


