import requests_mock
import pytest
import json
from requests import HTTPError

from app.web_requests.web_request import WebRequest
from app.settings import ROOT_DIR


@pytest.fixture()
def test_templates():
    with open(ROOT_DIR + r"\tests\data\web_request.json") as data_file:
        web_request_data = json.loads(data_file.read())
    return web_request_data


def test_get_ebay_access_token_correct(test_templates):
    with requests_mock.Mocker() as mock:
        mock.post(test_templates["get_ebay_access_token_url"], json=test_templates["get_ebay_access_token_response"], status_code=200)
        request = WebRequest(test_templates["get_ebay_access_token_url"],
                             test_templates["get_ebay_access_token_headers"],
                             test_templates["get_ebay_access_token_payload"])
        assert isinstance(request.response(), dict)


def test_get_ebay_access_token_error(test_templates):
    with requests_mock.Mocker() as mock:
        mock.post(test_templates["get_ebay_access_token_url"], json=test_templates["get_ebay_access_token_response"], status_code=404)
        with pytest.raises(HTTPError):
            request = WebRequest(test_templates["get_ebay_access_token_url"],
                                 test_templates["get_ebay_access_token_headers"],
                                 test_templates["get_ebay_access_token_payload"])
            request.response()


def test_get_orders_correct(test_templates):
    with requests_mock.Mocker() as mock:
        mock.get(test_templates["get_orders_url"], json=test_templates["get_orders_response"], status_code=200)
        request = WebRequest(test_templates["get_orders_url"], test_templates["get_orders_headers"])
        assert isinstance(request.response(), dict)


def test_get_orders_error(test_templates):
    with requests_mock.Mocker() as mock:
        mock.get(test_templates["get_orders_url"], json=test_templates["get_orders_response"], status_code=404)
        with pytest.raises(HTTPError):
            request = WebRequest(test_templates["get_orders_url"], test_templates["get_orders_headers"])
            request.response()


def test_get_order_correct(test_templates):
    with requests_mock.Mocker() as mock:
        mock.get(test_templates["get_order_url"], json=test_templates["get_order_response"], status_code=200)
        request = WebRequest(test_templates["get_order_url"], test_templates["get_order_headers"])
        assert isinstance(request.response(), dict)


def test_get_order_error(test_templates):
    with requests_mock.Mocker() as mock:
        mock.get(test_templates["get_order_url"], json=test_templates["get_order_response"], status_code=404)
        with pytest.raises(HTTPError):
            request = WebRequest(test_templates["get_order_url"], test_templates["get_order_headers"])
            request.response()


def test_create_invoice_correct(test_templates):
    with requests_mock.Mocker() as mock:
        mock.post(test_templates["create_invoice_url"], json=test_templates["create_invoice_response"], status_code=200)
        request = WebRequest(test_templates["create_invoice_url"],
                             test_templates["create_invoice_headers"],
                             test_templates["create_invoice_payload"])
        assert isinstance(request.response(), dict)


def test_create_invoice_error(test_templates):
    with requests_mock.Mocker() as mock:
        mock.post(test_templates["create_invoice_url"], json=test_templates["create_invoice_response"], status_code=404)
        with pytest.raises(HTTPError):
            request = WebRequest(test_templates["create_invoice_url"],
                                 test_templates["create_invoice_headers"],
                                 test_templates["create_invoice_payload"])
            request.response()
