import json
from test_data.data_openbrewerydb import openbrawerydb_get_data
import pytest
import requests
from jsonschema import validate

base_url = 'https://api.openbrewerydb.org/v1/breweries'

def request_method(method_string: str, url, **kwargs):
    return requests.get(url) if method_string.lower() == "get" else requests.post()



def test_test():
    responce = request_method("get", base_url + "/random")

    validate(instance=responce.json(), schema=openbrawerydb_get_data())
    print(responce.json())


    '''
    класс дог апи, там нужно - методы гет и пост(?) с юрл, валидация должна быть в нем
    '''