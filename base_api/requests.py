import requests


class Client:

    def request_method(self, method: str, url,  **kwargs):
        return requests.request(method, url, **kwargs)