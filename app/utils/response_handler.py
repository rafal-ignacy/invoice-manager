from dataclasses import dataclass
from typing import List


@dataclass
class ResponseHandler:
    def get_ebay_access_token(self, response) -> str:
        return response["access_token"]

    def get_orders(self, response) -> List:
        return response["orders"]

    def create_invoice(self, response) -> str:
        return response["id"]
