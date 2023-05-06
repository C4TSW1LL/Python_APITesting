import requests
from jsonschema import validate
from schemas.dog_schema import dog_schema
from base_api.requests import Client
from base_api.model import Model

class Request:
    def __init__(self, url, path):
        self.url = url
        self.client = Client()
        self.path = path


    def dog_get_request(self, dog_chema):
        responce = self.client.request_method(self.url + self.path)
        validate(instance=responce.json(), schema=dog_schema())
        return Model(status=responce.status_code, response=responce.json())