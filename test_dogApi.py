import pytest
import requests
from conftest import base_url
from jsonschema import validate
from base_api.dog_api import Request
from schemas.dog_schema import dog_schema

base_url = "https://dog.ceo/api/breed"


def test_test():
    responce = Request(url=base_url, path=).dog_get_request(dog_chema=dog_schema())
    print(base_url + "s/image/random")
    assert responce.status == 200
    assert responce.responce.get('status') == "success"







def test_get_random_image():
    schema =  {
        'type': 'object',
        'properties': {
            'address_1': {'type': 'string'}}}
    response = requests.get(base_url + "s" + "/image/random/")
    assert validate(instance=response.json(), schema=schema)

    assert response.status_code == 200
    assert response.json().get('status') == 'success'

def test_get_several_random_image(random_number):
    responce = requests.get(base_url + "s" + "/image/random/" + random_number)
    message_length = str(len(responce.json().get('message')))


    assert responce.status_code == 200
    assert responce.json().get('status') == 'success'
    assert message_length == random_number


def test_incorrect_get_several_random_image(random_number):
    responce = requests.get(base_url + "s" + "/image/random" + random_number)

    assert responce.status_code == 404
    assert responce.json().get('status') == 'error'


@pytest.mark.parametrize('path, message_type, code, status',
                        [("s/image/random", str, 200, 'success'),
                         ("s/image/random/3", list, 200, 'success'),
                         ("s/image/random3", str, 404, 'error'),
                         ("s/list/all", dict, 200, 'success')])
def test_check_message_type(path, message_type, code, status):
    responce = requests.get(base_url + path)

    assert responce.status_code == code
    assert type(responce.json().get('message')) == message_type


@pytest.mark.parametrize('dog_breed, path, code, status',
                         [('/african', '/images/random', 200, 'success'),
                          ('/psina', '/images/random', 404, 'error')])
def test_check(dog_breed, path, code, status):
    responce = requests.get(base_url + dog_breed + path)

    assert responce.status_code == code
    assert responce.json().get('status') == status

