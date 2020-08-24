from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class NewCustomer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

class NewCustomerSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    dob = fields.DateTime(required=True)
    updated_at = fields.DateTime()

class Customer(db.Model):
    __tablename__ = 'customers'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    

    def __init__(self, name, dob, id):
        self.name = name
        self.dob = dob
        self.id = id

class CustomerSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    dob = fields.DateTime()
    updated_at = fields.DateTime()