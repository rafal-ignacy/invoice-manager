import json
import pytest


from app.settings import ROOT_DIR
from app.web_requests.headers import Headers


@pytest.fixture()
def test_templates():
    headers = Headers()
    with open(ROOT_DIR + r"\tests\data\headers.json") as data_file:
        headers_data = json.loads(data_file.read())
    return {"class": headers, "data": headers_data}


def test_get_access_token(test_templates):
    assert test_templates["class"].get_ebay_access_token() == test_templates["data"]["get_access_token"]


def test_get_order(test_templates):
    assert test_templates["class"].get_order(test_templates["data"]["access_token"]) == test_templates["data"]["get_order"]


def test_get_orders(test_templates):
    assert test_templates["class"].get_order(test_templates["data"]["access_token"]) == test_templates["data"]["get_orders"]


def test_create_invoice(test_templates):
    assert test_templates["class"].create_invoice() == test_templates["data"]["create_invoice"]
