from dicttoxml import dicttoxml
from flasgger import swag_from
from flask import make_response, request
from flask_restful import Resource
from database_app.api import built_drivers_list


class Drivers(Resource):

    @swag_from('apidocs/drivers.yml')
    def get(self):
        order = request.args.get('order')
        out_format = request.args.get('format')
        resp = built_drivers_list(order)
        if out_format == 'json':
            headers = {'content-type': 'application/json'}
            return make_response(resp, 200, headers)
        elif out_format == 'xml':
            headers = {'content-type': 'application/xml'}
            xml = dicttoxml(resp,  attr_type=True)
            return make_response(xml, 200, headers)
        else:
            return {'message': 'Format field should be json or xml'}
