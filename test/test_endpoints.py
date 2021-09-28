import os
import requests
from openapi_spec_validator import validate_spec_url

def test_producto_test(api_v1_host):
    endpoint = api_v1_host + "/producto/test"
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "I'm the test endpoint from producto."


def test_codigoasin(api_v1_host):
    endpoint = api_v1_host + "/producto/codigoasin"
    payload = {'number': 5}
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "Your result is: '10'"



def test_swagger_specification(host):
    endpoint = host + '/api/swagger.json'
    validate_spec_url(endpoint)