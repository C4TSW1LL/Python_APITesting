import json

import pytest
import requests
from jsonschema import validate

base_url = 'https://api.openbrewerydb.org/v1/breweries'

def request_method(method_string: str, url, **kwargs):
    return requests.get(url) if method_string.lower() == "get" else requests.post()

def test_openbrawerydb_get_data():
    responce = request_method("get", base_url + "/random")



    schema = {
        'type': 'object',
        'properties': {
            'address_1': {'type': 'string'},
            'address_2': {'type': 'string'},
            'address_3': {'type': 'string'},
            'brewery_type': {'type': 'string'},
            'city': {'type': 'string'},
            'country': {'type': 'string'},
            'id': {'type': 'string'},
            'latitude': {'type': 'string'},
            'longitude': {'type': 'string'},
            'name': {'type': 'string'},
            'phone': {'type': 'string'},
            'postal_code': {'type': 'string'},
            'state': {'type': 'string'},
            'state_province': {'type': 'string'},
            'street': {'type': 'string'},
            'website_url': {'type': 'string'}
        },
        'required': ['id',
                     'name',
                     'brewery_type',
                     'address_1',
                     'address_2',
                     'address_3',
                     'city',
                     'state_province',
                     'postal_code',
                     'countrylongitude',
                     'latitude',
                     'phone',
                     'website_url',
                     'statestreet'],
        }
    validate(instance=responce.json(), schema=schema)
    # return schema
    # def get_brewery_list(n, url = base_url):
    #     responce = requests.get(base_url + "?per_page=" + n)
    #     res_json = responce.json()
    #     with open("user_data.json", "w") as f:
    #         s = json.dumps(res_json, indent=4)
    #         f.write(s)
    #     with open("user_data.json", "r") as f:
    #         data = json.loads(f.read())
    #
    #         for el in data:
    #             yield el
    #
    # user_data = get_brewery_list("3", base_url)
