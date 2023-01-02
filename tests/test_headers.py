import json
import pytest


from app.settings import ROOT_DIR
from app.web_requests.headers import Headers


@pytest.fixture()
def test_templates():
    with open(ROOT_DIR + r"\tests\data\headers.json") as data_file:
        headers_data = json.loads(data_file.read())
    return headers_data


def test_get_access_token(test_templates):
    headers = Headers()
    assert headers.get_ebay_access_token() == test_templates["get_access_token"]


def test_get_order(test_templates):
    headers = Headers()
    test_template = test_templates["get_order"]
    access_token = test_templates["access_token"]
    assert headers.get_order(access_token) == test_template


def test_get_orders(test_templates):
    headers = Headers()
    test_template = test_templates["get_orders"]
    access_token = test_templates["access_token"]
    assert headers.get_order(access_token) == test_template


def test_create_invoice(test_templates):
    headers = Headers()
    assert headers.create_invoice() == test_templates["create_invoice"]
