import pytest
import requests
from conftest import base_url
from base_api.dog_api import Request
from schemas.dog_schema import dog_schema

base_url = "https://dog.ceo/api/breed"

def test_get_random_image():
    response = Request(url=base_url, path="s/image/random",
                       schema=dog_schema, schema_data="string").dogApi_GET()

    assert response.status == 200
    assert response.response.get('status') == "success"
    assert response.response.get('message')

def test_get_several_random_image(random_number):
    response = Request(url=base_url, path="s/image/random/" + random_number,
                       schema=dog_schema, schema_data="array").dogApi_GET()


    assert response.status == 200
    assert response.response.get('status') == 'success'
    assert str(len(response.response.get('message'))) == random_number
    assert response.response.get('message')


def test_incorrect_get_several_random_image(random_number):
    response = Request(url=base_url, path="s/image/random" + random_number,
                       schema=dog_schema, schema_data="string").dogApi_GET()

    assert response.status == 404
    assert response.response.get('status') == 'error'
    assert response.response.get('message')


@pytest.mark.parametrize('path, message_type, code, status',
                        [("s/image/random", "string", 200, 'success'),
                         ("s/image/random/3", "array", 200, 'success'),
                         ("s/image/random3", "string", 404, 'error'),
                         ("/hound/images", "array", 200, 'success')])
def test_check_message_type(path, message_type, code, status):
    response = Request(url=base_url, path=path,
                       schema=dog_schema, schema_data=message_type).dogApi_GET()

    assert response.status == code
    assert response.response.get('status') == status
    assert response.response.get('message')

@pytest.mark.parametrize('dog_breed, path, code, message_type, status',
                         [('/african', '/images/random', 200, 'string', 'success'),
                          ('/psina', '/images/random', 404, 'string', 'error')])
def test_breed_list(dog_breed, path, code, message_type, status):
    response = Request(url=base_url + dog_breed, path=path,
                       schema=dog_schema, schema_data=message_type).dogApi_GET()

    assert response.status == code
    assert response.response.get('status') == status
    assert response.response.get('message')
