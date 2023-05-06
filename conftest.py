import random

import pytest

def pytest_addoption(parser):
    parser.addoption("--url")

@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def random_number():
    return str(random.randint(1, 10))