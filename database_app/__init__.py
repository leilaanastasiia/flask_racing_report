from flask import Flask, make_response, json
from flask_restful import Api
from simplexml import dumps
from flasgger import Swagger
from database_app.models import init_db
from database_app.resources.drivers import Drivers
from database_app.resources.drivers_abb import DriversAbb
from database_app.resources.index import Index
from database_app.resources.report import Report


app = Flask(__name__)
api = Api(app, default_mediatype='application/json')

app.config['SWAGGER'] = {
    'title': 'Flasgger Report API',
    'uiversion': 3}

swag = Swagger(app)
PREFIX1 = '/api/v1'


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps({'Response': data}), code)
    resp.headers.extend(headers or {})
    return resp


@api.representation('application/xml')
def output_xml(data, code, headers=None):
    resp = make_response(dumps({'Response': data}), code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(Index, '/')
api.add_resource(Report, PREFIX1 + '/report/')
api.add_resource(Drivers, PREFIX1 + '/report/drivers/')
api.add_resource(DriversAbb, PREFIX1 + '/report/drivers/<path:drivers_abb>/')

init_db()

if __name__ == '__main__':
    app.run(debug=True)
