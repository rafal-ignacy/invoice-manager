import pytest
import json


from app.settings import ROOT_DIR
from app.web_requests.urls import Urls


@pytest.fixture()
def test_templates():
    urls = Urls()
    with open(ROOT_DIR + r"\tests\data\urls.json") as data_file:
        urls_data = json.loads(data_file.read())
    return {"class": urls, "data": urls_data}


def test_get_access_token(test_templates):
    assert test_templates["class"].get_access_token() == test_templates["data"]["get_access_token"]


@pytest.mark.parametrize("order_id", [("5351206652")])
def test_get_order(test_templates, order_id):
    assert test_templates["class"].get_order(order_id) == test_templates["data"]["get_order"]


@pytest.mark.parametrize("date", [("2023-01-03T22:00:00.000Z")])
def test_get_orders(test_templates, date):
    assert test_templates["class"].get_orders(date) == test_templates["data"]["get_orders"]


def test_create_invoice(test_templates):
    assert test_templates["class"].create_invoice() == test_templates["data"]["create_invoice"]
