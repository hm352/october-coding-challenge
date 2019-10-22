from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

company_numbers = {}

class CompanyId(Resource):
    def get(self):
        return company_numbers

    def post(self):
    	return {'hello': 'world'}

api.add_resource(CompanyId, '/')


if __name__ == '__main__':
    app.run(debug=True)