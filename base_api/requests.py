import requests


class Client:

    def request_method(method: str, url, path, **kwargs):
        return requests.get(url) #if method.lower() == "get" else requests.post(url)
        # return requests.request(method, url, **kwargs)