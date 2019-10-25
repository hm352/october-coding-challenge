from flask import Flask
from flask_restful import Resource, Api, reqparse
from googleapiclient.discovery import build
from re import search 


app = Flask(__name__)
api = Api(app)

company_numbers = {}

parser = reqparse.RequestParser()
parser.add_argument('company', required=True)

def is_number(number):
    # checks format of phone number
    # returns boolean
    return number


class CompanyId(Resource):
    # defines API
    def get(self):
        return company_numbers

    def post(self):
        # Returns number for a given company name
        args = parser.parse_args()
        company = args.get('company', None)
        if company:
            """ Uses a custom search engine that searches
            the domain https://www.verif.com/*
            considered screen scraping link but phone number is
            provided as part of url
            """
            service = build("customsearch", "v1", developerKey="API_KEY")
            result = service.cse().list(
                q=company,
                cx='CSE_ID'
            ).execute()
            url = result['items'][0]['link'].split('/')
            number =  is_number(url[-2].split('-')[-1])

            if number:
                company_numbers[company] = number

            return (number)


# adds CompanyId to base url
api.add_resource(CompanyId, '/')

if __name__ == '__main__':
    app.run(debug=True)
