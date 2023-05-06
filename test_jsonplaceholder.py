import pytest
import requests
from conftest import base_url
import json

base_url = "https://jsonplaceholder.typicode.com"

def test_get_users(url = base_url, number_of_users = 100):
    response = requests.get(base_url + "/posts")
    count_users = len(response.json())

    assert response.status_code == 200
    assert count_users == number_of_users


def test_get_the_first_user(url = base_url):
    response = requests.get(base_url + "/posts/1")

    assert response.status_code == 200
    assert response.json().get('userId') == 1
    assert response.json().get('id') == 1


@pytest.mark.parametrize('input_title, output_title',
                        [("kotiki is cool", "kotiki is cool"),
                         ("sobachki is cool", "sobachki is cool")])
def test_post_by_title(input_title, output_title, url = base_url):

    data = {"title": input_title,
            "body": "this is body text for this test request",
            "userId": 1}

    response = requests.post(base_url + "/posts",json=data,verify=False)

    assert response.status_code == 200
    assert response.json().get('title') == output_title
    assert response.json().get('body') == 'this is body text for this test request'
    assert response.json().get('userId') == 1

@pytest.mark.parametrize('customers_number', (0, 1, 2, 3, 4))
@pytest.mark.parametrize('postId', ('1', '2', '3', '4', '5'))
def test_get_comments(postId, customers_number, url = base_url):
    response = requests.get(base_url + "/posts/" + postId + "/comments")

    assert response.status_code == 200
    assert response.json()[customers_number]['postId'] == int(postId)

def test_check_body(url = base_url):
    response = requests.get(base_url + "/posts/1")

    assert response.status_code == 200
    assert response.json().get("body") == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

  