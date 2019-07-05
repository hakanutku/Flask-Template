import datetime
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Customers(db.Model):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'customer'}

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(350), nullable=False)
    slug_name = db.Column(db.String(150))
    users = db.relationship('CustomerUsers', back_populates='customer')


class CustomerUsers(db.Model):
    __tablename__ = 'customer_users'
    __table_args__ = {'schema': 'customer'}

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    user_name = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(500))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customers.customer_id'))
    customer = db.relationship('Customers', back_populates='users')

    def set_password(self, password):
        self.password_hash = password
        # self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # return check_password_hash(self.password_hash, password)
        return self.password_hash == password

    def create_token(self, expires_in=datetime.timedelta(60*60*24)):
        return create_access_token(identity=self.user_id, expires_delta=expires_in)