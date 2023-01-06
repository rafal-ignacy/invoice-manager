from dataclasses import dataclass
from typing import Dict, List
import json


from app.settings import ROOT_DIR
from app.web_requests.request_component import RequestComponent


@dataclass
class Payloads(RequestComponent):
    def __init__(self) -> None:
        self.__payloads = self.get_file_data_dict(ROOT_DIR + r"\app\data\payloads.json")
        self.__credentials = self.get_file_data_dict(ROOT_DIR + r"\app\data\credentials.json")

    def get_ebay_access_token(self) -> Dict:
        payload: Dict = self.__payloads["get_ebay_access_token"]
        payload["refresh_token"] = payload["refresh_token"].replace("{refresh_token}", self.__credentials["ebay_refresh_token"])
        return payload

    def create_invoice(self, order_data: Dict) -> Dict:
        payload: str = json.dumps(self.__payloads["create_invoice"])
        return json.loads(self.replace_invoice_payload(payload, order_data))

    def replace_invoice_payload(self, payload: str, order_data: Dict) -> str:
        for invoice_key in order_data.keys():
            if invoice_key != "{items}":
                payload = payload.replace(invoice_key, order_data[invoice_key])
            else:
                items_payload_str = self.replace_items(order_data[invoice_key])
                payload = payload.replace("\"{items}\"", items_payload_str)
        return payload

    def replace_items(self, items: List) -> str:
        items_invoice: List = []
        for item in items:
            item_invoice = json.dumps(self.__payloads["replace_item_payload"])
            for item_key in item.keys():
                item_invoice = item_invoice.replace(item_key, item[item_key])
            items_invoice.append(item_invoice)
        items_invoice_str: str = ", ". join(item for item in items_invoice)
        return items_invoice_str
