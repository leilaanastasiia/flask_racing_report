from dicttoxml import dicttoxml
from flasgger import swag_from
from flask import make_response, request
from flask_restful import Resource
from database_app.api import search_by_abb


class DriversAbb(Resource):

    @swag_from('apidocs/drivers_abb.yml')
    def get(self, drivers_abb):
        out_format = request.args.get('format')
        data = search_by_abb(drivers_abb)
        resp = {'name': data[0],
                'car': data[1],
                'time': data[2]}
        if out_format == 'json':
            headers = {'content-type': 'application/json'}
            return make_response(resp, 200, headers)
        elif out_format == 'xml':
            headers = {'content-type': 'application/xml'}
            xml = dicttoxml(resp,  attr_type=True)
            return make_response(xml, 200, headers)
        else:
            return {'message': 'Format field should be json or xml'}
