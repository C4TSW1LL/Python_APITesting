import requests
from jsonschema import validate
from schemas.open_brewery_schema import open_brewery_schema
from base_api.requests import Client
from base_api.model import Model


class Request:
    def __init__(self, url, path, schema, schema_data):
        self.url = url
        self.client = Client()
        self.path = path
        self.schema = open_brewery_schema(schema_data)

    def open_brewery_GET(self):
        response = self.client.request_method("GET", self.url + self.path)
        validate(instance=response.json(), schema=self.schema)
        return Model(status=response.status_code, response=response.json())
