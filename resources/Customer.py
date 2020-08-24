import json
from flask_jwt import jwt_required

from flask import request
from flask_restful import Resource
from Model import db, NewCustomer, NewCustomerSchema, Customer, CustomerSchema

customers_schema = NewCustomerSchema(many=True)
new_customer_schema = NewCustomerSchema()
customer_schema = CustomerSchema()

class CustomerList(Resource):
    @jwt_required()
    def get(self, id):
        customers = Customer.query.order_by(Customer.dob).limit(id).all()
        customers = customers_schema.dump(customers).data
        return {'status': 'success', 'data': customers}, 200

class CustomerResource(Resource):
    def get(self):
        customers = Customer.query.all()
        customers = customers_schema.dump(customers).data
        return {'status': 'success', 'data': customers}, 200

    @jwt_required()
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = new_customer_schema.load(json_data)
        if errors:
            return errors, 422
        customer = NewCustomer.query.filter_by(name=data['name']).first()
        if customer:
            return {'message': 'Customer already exists'}, 400
        customer = NewCustomer(
        name=json_data['name'],
        dob=json_data['dob']
        )

        db.session.add(customer)
        db.session.commit()

        result = new_customer_schema.dump(customer).data

        return { "status": 'success', 'data': result }, 201

    @jwt_required()
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = customer_schema.load(json_data)
        if errors:
            return errors, 422
        customer = Customer.query.filter_by(id=data['id']).first()
        if not customer:
            return {'message': 'Customer does not exist'}, 400
        if customer.name:
            customer.name = data['name']
        if customer.dob:
            customer.dob = data['dob']
        db.session.commit()

        result = customer_schema.dump(customer).data

        return { "status": 'success', 'data': result }, 204

    @jwt_required()
    def delete(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = customer_schema.load(json_data)
        if errors:
            return errors, 422
        customer = Customer.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = customer_schema.dump(customer).data

        return { "status": 'success', 'data': result}, 204