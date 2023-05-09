import requests
from jsonschema import validate
from schemas.dog_schema import dog_schema
from dog_api.requests import Client
from dog_api.model import Model


class Request:
    def __init__(self, url, path, schema, schema_data):
        self.url = url
        self.client = Client()
        self.path = path
        self.schema = dog_schema(schema_data)

    def dogApi_GET(self):
        response = self.client.request_method("GET", self.url + self.path)
        validate(instance=response.json(), schema=self.schema)
        return Model(status=response.status_code, response=response.json())
