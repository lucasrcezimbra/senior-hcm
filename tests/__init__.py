import json

from requests import Response


def create_fake_response(dict_response, status_code=200):
    response = Response()
    response.status_code = status_code
    response._content = bytes(json.dumps(dict_response).encode('utf-8'))
    return response
