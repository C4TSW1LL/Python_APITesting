import requests


def test_status_code(base_url):
    request = requests.get(base_url[0])
    assert request.status_code == base_url[1]