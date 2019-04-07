from unittest.mock import MagicMock

import pytest

from senior_hcm import SeniorHcm
from tests import create_fake_response


@pytest.fixture
def senior(login_response_mock, monkeypatch):
    response = create_fake_response(login_response_mock)
    monkeypatch.setattr('requests.Session.post',
                        MagicMock(return_value=response))
    return SeniorHcm(email='example@mail.com', password='password')


def test_get_recents_payrolls(senior, monkeypatch, payrolls_response_mock):
    fake_response = create_fake_response(payrolls_response_mock)
    get_mock = MagicMock(return_value=fake_response)
    monkeypatch.setattr('requests.Session.get', get_mock)

    payrolls = senior.get_recent_payrolls()

    api_root_url = 'https://hcm-api.senior.com.br/frontend-api/'
    expected_url = api_root_url + f'payrollregister/recents/{senior.user_id}'

    get_mock.assert_called_once_with(expected_url)
    assert payrolls == payrolls_response_mock


def test_get_last_payroll(senior, monkeypatch, payrolls_response_mock):
    fake_response = create_fake_response(payrolls_response_mock)
    get_mock = MagicMock(return_value=fake_response)
    monkeypatch.setattr('requests.Session.get', get_mock)

    last_payroll = senior.get_last_payroll()

    assert last_payroll == payrolls_response_mock['list'][0]
