from flasgger import swag_from
from flask import make_response
from flask_restful import Resource


class Index(Resource):

    @swag_from('apidocs/index.yml')
    def get(self):
        headers = {'content-type': 'application/json'}
        resp = {
            'Report': 'http://127.0.0.1:5000/api/v1/report/?order=asc&format=json',
            'Drivers': 'http://127.0.0.1:5000/api/v1/report/drivers/?order=asc&format=json',
        }
        return make_response(resp, 200, headers)
