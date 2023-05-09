import pytest
import requests
from conftest import base_url
from base_api.jsonplaceholder_api import Request
from schemas.jsonplaceholder_schema import jsonplaceholder_schema
from jsonschema import validate

base_url = "https://jsonplaceholder.typicode.com"


def test_get_post_1():
    response = Request(url=base_url, path="/posts/1",
                       schema=jsonplaceholder_schema, schema_data="posts").jsonplaceholder_GET()

    assert response.status == 200
    assert response.response.get('userId') == 1
    assert response.response.get('id') == 1


def test_get_the_first_user(random_number):
    response = Request(url=base_url, path="/posts/" + random_number,
                       schema=jsonplaceholder_schema, schema_data="posts").jsonplaceholder_GET()

    assert response.status == 200
    assert response.response.get('userId') == 1
    assert response.response.get('id') == int(random_number)


@pytest.mark.parametrize('input_title, output_title',
                         [("kotiki is cool", "kotiki is cool"),
                          ("sobachki is cool", "sobachki is cool")])
def test_post_by_title(input_title, output_title, url=base_url):
    data = {"type": "object",
            "properties": {
                "id": 101,
                "title": input_title,
                "body": 'this is body text for this test request'}}

    response = Request(url=base_url, path="/posts",
                       schema=jsonplaceholder_schema,
                       schema_data="posts").jsonplaceholder_POST(json=data, verify=False)

    assert response.status == 200
    assert response.response.get('userId') == 1


@pytest.mark.parametrize('position, schema, userId, id, title, status_code',
                         [('1', 'posts', 1, 1,
                           'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 200),
                          ('100', 'posts', 10, 100, 'at nam consequatur ea labore ea harum', 200),
                          ('101', 'empty', None, None, None, 404)])
def test_albums_request(position, schema, userId, id, title, status_code):
    response = Request(url=base_url, path=f'/posts/{position}',
                       schema=jsonplaceholder_schema, schema_data=schema).jsonplaceholder_GET()

    assert response.status == status_code
    assert response.response.get('userId') == userId
    assert response.response.get('id') == id
    assert response.response.get('title') == title


@pytest.mark.parametrize('position, schema, albumId, id, title, url, thumbnailUrl, status_code',
                         [('1', 'photos', 1, 1, 'accusamus beatae ad facilis cum similique qui sunt',
                           'https://via.placeholder.com/600/92c952', 'https://via.placeholder.com/150/92c952', 200),
                          ('5000', 'photos', 100, 5000, 'error quasi sunt cupiditate voluptate ea odit beatae',
                           'https://via.placeholder.com/600/6dd9cb', 'https://via.placeholder.com/150/6dd9cb', 200),
                          ('5001', 'empty', None, None, None, None, None, 404)]
                         )
def test_photos_request(position, schema, albumId, id, title, url, thumbnailUrl, status_code):
    response = Request(url=base_url, path=f'/photos/{position}',
                       schema=jsonplaceholder_schema, schema_data=schema).jsonplaceholder_GET()

    assert response.status == status_code
    assert response.response.get('albumId') == albumId
    assert response.response.get('id') == id
    assert response.response.get('title') == title
    assert response.response.get('url') == url
    assert response.response.get('thumbnailUrl') == thumbnailUrl
