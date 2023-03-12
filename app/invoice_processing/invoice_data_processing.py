from dataclasses import dataclass
from typing import Tuple, Dict
import json

from app.settings import ROOT_DIR
from app.utils.date_handler import DateHandler
from app.utils.exchange_rate_handler import ExchangeRateHandler


@dataclass
class InvoiceDataProcessing:
    def __init__(self):
        self.items_names: Dict = self.get_json(ROOT_DIR + r"/app/data/items_names.json")  # type: ignore

    def get_json(self, path) -> Dict:
        with open(path, "r", encoding="utf-8") as json_file:
            json_data = json.loads(json_file.read())
        return json_data

    def get_invoice_details_dict(self, invoice_details: Tuple) -> Dict:
        invoice_details_dict: Dict = {}
        date_handler = DateHandler()
        exchange_rate_handler = ExchangeRateHandler()
        SERVICE_DATE, CURRENCY, PAID_AMOUNT = 1, 2, 3
        invoice_details_dict["issue_date"] = date_handler.current_date()
        service_date = date_handler.payment_date_local_zone(invoice_details[SERVICE_DATE])
        invoice_details_dict["service_date"] = service_date
        invoice_details_dict["currency"] = invoice_details[CURRENCY]
        invoice_details_dict["paid_amount"] = str(invoice_details[PAID_AMOUNT])
        invoice_details_dict["rate"] = exchange_rate_handler.set_exchange_rate(service_date, invoice_details[CURRENCY])
        return invoice_details_dict

    def get_invoice_customer_details_dict(self, customer_details: Tuple) -> Dict:
        customer_details_dict: Dict = {}
        EMAIL, FULL_NAME, ADDRESS_STREET1, ADDRESS_STREET2,  = 0, 1, 2, 3
        CITY, POST_CODE, STATE_OR_PROVINCE, COUNTRY_CODE = 4, 5, 6, 7
        customer_details_dict["email"] = customer_details[EMAIL]
        customer_details_dict["full_name"] = customer_details[FULL_NAME]
        customer_details_dict["address_street"] = customer_details[ADDRESS_STREET1]
        customer_details_dict["city"] = customer_details[CITY]
        customer_details_dict["post_code"] = customer_details[POST_CODE]
        customer_details_dict["country_code"] = customer_details[COUNTRY_CODE]
        customer_details_dict["tax_country_code"] = customer_details[COUNTRY_CODE]
        if customer_details[ADDRESS_STREET2] is not None:
            customer_details_dict["address_street"] = customer_details_dict["address_street"] + ", " + customer_details[ADDRESS_STREET2]
        if customer_details[STATE_OR_PROVINCE] is not None:
            if customer_details[COUNTRY_CODE] != "US":
                customer_details_dict["address_street"] = customer_details_dict["address_street"] + ", " + customer_details[STATE_OR_PROVINCE]
            else:
                customer_details_dict["post_code"] = customer_details[STATE_OR_PROVINCE] + " " + customer_details_dict["post_code"]
        return customer_details_dict

    def get_invoice_item_details_dict(self, item_details: Tuple) -> Dict:
        item_details_dict: Dict = {}
        SKU, QUANTITY, PRICE = 0, 1, 2
        item_details_dict["name"] = self.get_invoice_item_position_name(item_details[SKU])
        item_details_dict["code"] = item_details[SKU]
        item_details_dict["quantity"] = str(item_details[QUANTITY])
        item_details_dict["price"] = str(item_details[PRICE])
        return item_details_dict

    def get_invoice_item_position_name(self, sku: str) -> str | None:
        item_type: str = ''.join(char for char in sku if char.isalpha())
        item_position_name = self.items_names.get(item_type)
        return item_position_name

    def get_shipping_details_dict(self, shipping_price: str):
        shipping_details_dict = {}
        shipping_details_dict["name"] = self.items_names.get("SHIPPING")
        shipping_details_dict["code"] = None
        shipping_details_dict["quantity"] = "1"
        shipping_details_dict["price"] = str(shipping_price)
        return shipping_details_dict
