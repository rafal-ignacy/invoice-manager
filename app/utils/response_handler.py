from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ResponseHandler:
    def get_ebay_access_token(self, response: Dict) -> str:
        return response["access_token"]

    def get_ebay_orders(self, response: Dict) -> List:
        return response["orders"]

    def create_invoice(self, response: Dict) -> int:
        return response["id"]

    def exchange_rate(self, response: Dict) -> str:
        return str(response["rates"][0]["mid"])

    def get_etsy_access_token(self, response: Dict) -> str:
        return response["access_token"]

    def get_etsy_refresh_token(self, response: Dict) -> str:
        return response["refresh_token"]

    def get_etsy_orders(self, response: Dict) -> List:
        return response["results"]
