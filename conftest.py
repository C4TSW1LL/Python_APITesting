import random

import pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru")
    parser.addoption("--status_code", action="store", default=200)

@pytest.fixture
def base_url(request):
    url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    return url, status_code

@pytest.fixture
def random_number():
    return str(random.randint(1, 10))