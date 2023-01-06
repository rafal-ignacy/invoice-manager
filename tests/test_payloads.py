import pytest
import json


from app.web_requests.payloads import Payloads
from app.settings import ROOT_DIR


@pytest.fixture()
def test_templates():
    payloads = Payloads()
    with open(ROOT_DIR + r"\tests\data\payloads.json") as data_file:
        payloads_data = json.loads(data_file.read())
    return {"class": payloads, "data": payloads_data}


def test_get_ebay_access_token(test_templates):
    assert test_templates["class"].get_ebay_access_token() == test_templates["data"]["get_access_token"]


def test_create_invoice(test_templates):
    result = test_templates["class"].create_invoice(test_templates["data"]["create_invoice_orders_data"])
    assert result == test_templates["data"]["create_invoice_template_final"]


def test_replace_invoice_payload(test_templates):
    template_payload = json.dumps(test_templates["data"]["replace_invoice_payload_template_payload"])
    template_orders_data = test_templates["data"]["create_invoice_orders_data"]
    result = test_templates["class"].replace_invoice_payload(template_payload, template_orders_data)
    assert result == json.dumps(test_templates["data"]["create_invoice_template_final"])


def test_replace_item(test_templates):
    template_final = json.dumps(test_templates["data"]["replace_items_template_final"])
    assert test_templates["class"].replace_items(test_templates["data"]["replace_items_items_data"]) == template_final
