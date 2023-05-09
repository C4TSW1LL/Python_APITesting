import requests
from jsonschema import validate
from schemas.jsonplaceholder_schema import jsonplaceholder_schema
from base_api.requests import Client
from base_api.model import Model


class Request:
    def __init__(self, url, path, schema, schema_data):
        self.url = url
        self.client = Client()
        self.path = path
        self.schema = jsonplaceholder_schema(schema_data)

    def jsonplaceholder_GET(self):
        response = self.client.request_method("GET", self.url + self.path)
        validate(instance=response.json(), schema=self.schema)
        return Model(status=response.status_code, response=response.json())

    def jsonplaceholder_POST(self, json, verify):
        response = self.client.request_method("POST", self.url + self.path)
        validate(instance=response.json(), schema=self.schema)
        return Model(status=response.status_code, response=response.json())