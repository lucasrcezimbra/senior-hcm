import json
from unittest.mock import MagicMock

import pytest
from requests import Response

from senior_hcm import SeniorHcm, LoginError
from tests import create_fake_response


def test_post_login(monkeypatch, login_response_mock):
    fake_response = create_fake_response(login_response_mock)
    post_mock = MagicMock(return_value=fake_response)
    monkeypatch.setattr('requests.Session.post', post_mock)

    email = 'example@mail.com'
    password = 'password'

    SeniorHcm(email=email, password=password)

    expected_url = 'https://hcm-api.senior.com.br/frontend-api/login'
    expected_data = json.dumps({'email': email, 'password': password})
    expected_headers = {'content-type': 'application/json;charset=UTF-8'}

    post_mock.assert_called_once_with(
        expected_url, data=expected_data, headers=expected_headers)


@pytest.mark.parametrize("http_status_not_200", [
    100, 101, 102, 103,
    201, 202, 203, 204, 205, 206, 207, 208, 226,
    300, 301, 302, 303, 304, 305, 306, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414,
    415, 416, 417, 418, 420, 421, 422, 423, 424, 426, 428, 429, 431, 440, 444,
    449, 450, 451, 495, 496, 497, 498, 499,
    500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 520, 521, 522,
    523, 524, 525, 526, 527, 530, 598
])
def test_login_error(http_status_not_200, monkeypatch):
    email = 'example@mail.com'
    password = 'password'

    response = Response()
    response.status_code = http_status_not_200
    monkeypatch.setattr('requests.Session.post',
                        MagicMock(return_value=response))

    with pytest.raises(LoginError):
        SeniorHcm(email=email, password=password)


def test_set_user_id(monkeypatch, login_response_mock, user_id):
    fake_response = create_fake_response(login_response_mock)
    monkeypatch.setattr('requests.Session.post',
                        MagicMock(return_value=fake_response))

    senior = SeniorHcm(email='example@mail.com', password='password')

    assert senior.user_id == user_id
