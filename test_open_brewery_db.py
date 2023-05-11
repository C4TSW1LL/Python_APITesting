import pytest
import requests
from conftest import base_url
from base_api.open_brewery_db_api import Request
from schemas.open_brewery_schema import open_brewery_schema



base_url = "https://api.openbrewerydb.org"


def test_single_brewery():
    response = Request(url=base_url, path='/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0',
                       schema=open_brewery_schema, schema_data="object").open_brewery_GET()

    assert response.status == 200
    assert response.response.get('id') == 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'
    assert response.response.get('name') == "MadTree Brewing 2.0"


def test_random_brewery():
    response = Request(url=base_url, path='/breweries/random',
                       schema=open_brewery_schema, schema_data="array").open_brewery_GET()
    assert response.status == 200
    assert response.response[0].get('id')
    assert response.response[0].get('name')


@pytest.mark.parametrize('city, schema, id, name',
                         [('san_diego', 'array', 'ef970757-fe42-416f-931d-722451f1f59c', '10 Barrel Brewing Co'),
                          ('san_francisco', 'array', '8f9621dc-da98-4ddb-82a1-039c9e2b3224', '21st Amendment Brewery Cafe'),
                          ('ulyanovsk', 'empty', None, None)]
                         )
def test_by_city(city, schema, id, name):
    response = Request(url=base_url, path=f'/breweries?by_city={city}&per_page=1',
                       schema=open_brewery_schema, schema_data=schema).open_brewery_GET()
    assert response.status == 200
    if schema != 'empty':
        assert response.response[0].get('id') == id
        assert response.response[0].get('name') == name


@pytest.mark.parametrize('schema, id, name',
                         [('array', '1e40495c-ca51-455d-a24b-6769efc04060', 'Circle 9 Brewing'),
                          ('array', 'b1f636c4-b1b6-44dc-9ea5-637da406d097', 'Seven Stills'),
                          ('empty', None, 'Hmelnoy house')]
                         )
def test_by_name(schema, id, name):
    response = Request(url=base_url, path=f'/breweries?by_name={name}&per_page=1',
                       schema=open_brewery_schema, schema_data=schema).open_brewery_GET()
    assert response.status == 200
    if schema != 'empty':
        assert response.response[0].get('id') == id
        assert response.response[0].get('name') == name


@pytest.mark.parametrize('state, schema, id, name',
                         [('new_york', 'array', 'd81ff708-b5d2-478f-af6a-6d40f5beb9ac', '12 Gates Brewing Company'),
                          ('washington', 'array', '03118499-a3d0-4c22-860d-4529509ae095', '101 Brewery'),
                          ('ulyanovskya_oblast', 'empty', None, None)]
                         )
def test_by_state(state, schema, id, name):
    response = Request(url=base_url, path=f'/breweries?by_state={state}&per_page=1',
                       schema=open_brewery_schema, schema_data=schema).open_brewery_GET()
    assert response.status == 200
    if schema != 'empty':
        assert response.response[0].get('id') == id
        assert response.response[0].get('name') == name
