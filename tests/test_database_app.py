import json
import simplexml
from mocking_data import START, END, ABB


###################################################################
def test_index(client):
    example_output = {
        "Drivers": "http://127.0.0.1:5000/api/v1/report/drivers/?order=asc&format=json",
        "Report": "http://127.0.0.1:5000/api/v1/report/?order=asc&format=json"
    }
    response = client.get('/')
    decoded_data = json.loads(response.data)
    assert example_output == decoded_data
    assert response.status_code == 200


####################################################################
def test_report_asc_json(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/?order=asc&format=json')
    decoded_data = json.loads(response.data)
    assert decoded_data['1']['name'] == "Sebastian Vettel"
    assert decoded_data['1']['car'] == "FERRARI"
    assert decoded_data['1']['time'] == 64.415


def test_report_desc_json(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/?order=desc&format=json')
    decoded_data = json.loads(response.data)
    assert decoded_data['1']['name'] == "Lewis Hamilton"
    assert decoded_data['1']['car'] == "MERCEDES"
    assert decoded_data['1']['time'] == 407.545


def test_report_asc_xml(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/?order=asc&format=xml')
    decoded_data = simplexml.loads(response.data)
    assert decoded_data['root']['n1']['name'] == "Sebastian Vettel"
    assert decoded_data['root']['n1']['car'] == "FERRARI"
    assert decoded_data['root']['n1']['time'] == '64.415'


def test_report_desc_xml(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/?order=desc&format=xml')
    decoded_data = simplexml.loads(response.data)
    assert decoded_data['root']['n1']['name'] == "Lewis Hamilton"
    assert decoded_data['root']['n1']['car'] == "MERCEDES"
    assert decoded_data['root']['n1']['time'] == '407.545'


####################################################################
def test_drivers_asc_json(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/drivers/?order=asc&format=json')
    decoded_data = json.loads(response.data)
    assert decoded_data['1']['link'] == "http://127.0.0.1:5000/api/v1/report/drivers/BHS/?format=json"
    assert decoded_data['1']['name'] == "Brendon Hartley"


def test_drivers_desc_json(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/drivers/?order=desc&format=json')
    decoded_data = json.loads(response.data)
    assert decoded_data['1']['link'] == "http://127.0.0.1:5000/api/v1/report/drivers/VBM/?format=json"
    assert decoded_data['1']['name'] == "Valtteri Bottas"


def test_drivers_asc_xml(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/drivers/?order=asc&format=xml')
    decoded_data = simplexml.loads(response.data)
    assert decoded_data['root']['n1']['link'] == "http://127.0.0.1:5000/api/v1/report/drivers/BHS/?format=json"
    assert decoded_data['root']['n1']['name'] == "Brendon Hartley"


def test_drivers_desc_xml(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/drivers/?order=desc&format=xml')
    decoded_data = simplexml.loads(response.data)
    assert decoded_data['root']['n1']['link'] == "http://127.0.0.1:5000/api/v1/report/drivers/VBM/?format=json"
    assert decoded_data['root']['n1']['name'] == "Valtteri Bottas"


####################################################################
def test_drivers_abb_json(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/drivers/SVF/?format=json')
    decoded_data = json.loads(response.data)
    assert decoded_data['name'] == "Sebastian Vettel"
    assert decoded_data['car'] == "FERRARI"
    assert decoded_data['time'] == 64.415


def test_drivers_abb_xml(client, mocker):
    mocker.patch('logic.reporting.parse_abb', return_value=ABB)
    mocker.patch('logic.time_operations.parse_start', return_value=START)
    mocker.patch('logic.time_operations.parse_end', return_value=END)
    response = client.get('/api/v1/logic/drivers/SVF/?format=xml')
    decoded_data = simplexml.loads(response.data)
    assert decoded_data['root']['name'] == "Sebastian Vettel"
    assert decoded_data['root']['car'] == "FERRARI"
    assert decoded_data['root']['time'] == '64.415'
