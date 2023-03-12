from dataclasses import dataclass
from typing import Dict
import json

from app.settings import ROOT_DIR
from app.web_requests.request_component import RequestComponent
from app.data_models.invoice.invoice_details import InvoiceDetails
from app.utils.invoice_payload_handler import InvoicePayloadHandler


@dataclass
class Payloads(RequestComponent):
    def __init__(self) -> None:
        self.__payloads = self.get_file_data_dict(ROOT_DIR + r"/app/data/payloads.json")
        self.__credentials = self.get_file_data_dict(ROOT_DIR + r"/app/data/credentials.json")

    def get_ebay_access_token(self) -> Dict:
        payload: Dict = self.__payloads["get_ebay_access_token"]
        payload["refresh_token"] = payload["refresh_token"].replace("{refresh_token}", self.__credentials["ebay_refresh_token"])
        return payload

    def create_invoice(self, invoice_details: InvoiceDetails):
        invoice_payload_handler = InvoicePayloadHandler()
        payload = self.__payloads["create_invoice"]
        payload["buyer"] = invoice_payload_handler.replace_customer_details(self.__payloads["customer_payload"], invoice_details.customer_details)
        payload["positions"] = invoice_payload_handler.replace_items_details(self.__payloads["item_payload"], invoice_details.items_details)
        payload = json.dumps(payload)
        payload_replace_elements = {"{issue_date}": invoice_details.issue_date, "{service_date}":  invoice_details.service_date, "{currency}": invoice_details.currency, "{rate}": invoice_details.rate}
        for key, value in payload_replace_elements.items():
            payload = payload.replace(key, value)
        if invoice_details.paid_amount is not None:
            payload = payload.replace("{paid_amount}", invoice_details.paid_amount)
        else:
            payload = payload.replace("{paid_amount}", "0")
        return payload.encode("utf-8")

    def get_etsy_access_token(self) -> Dict:
        payload: Dict = self.__payloads["get_etsy_access_token"]
        payload["client_id"] = payload["client_id"].replace("{client_id}", self.__credentials["etsy_client_id"])
        payload["refresh_token"] = payload["refresh_token"].replace("{refresh_token}", self.__credentials["etsy_refresh_token"])
        return payload
