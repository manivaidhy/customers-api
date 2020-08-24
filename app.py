from flask import Blueprint
from flask_restful import Api
from resources.Customer import CustomerResource, CustomerList

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(CustomerResource, '/Customer')
api.add_resource(CustomerList, '/Customer/<int:id>')