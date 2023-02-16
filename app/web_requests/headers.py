from dataclasses import dataclass
from typing import Dict


from app.settings import ROOT_DIR
from app.web_requests.request_component import RequestComponent


@dataclass
class Headers(RequestComponent):
    def __init__(self) -> None:
        self.__headers = self.get_file_data_dict(ROOT_DIR + r"\app\data\headers.json")
        self.__credentials: Dict = self.get_file_data_dict(ROOT_DIR + r"\app\data\credentials.json")

    def get_ebay_access_token(self) -> Dict:
        headers: Dict = self.__headers["get_ebay_access_token"]
        headers["Authorization"] = headers["Authorization"].replace("{base64_encoded_credentials}", self.__credentials["ebay_base64_encoded_credentials"])
        return headers

    def get_orders(self, access_token: str) -> Dict:
        headers: Dict = self.__headers["get_orders"]
        headers["Authorization"] = headers["Authorization"].replace("{ebay_access_token}", access_token)
        return headers

    def get_order(self, access_token: str) -> Dict:
        headers: Dict = self.__headers["get_order"]
        headers["Authorization"] = headers["Authorization"].replace("{ebay_access_token}", access_token)
        return headers

    def create_invoice(self) -> Dict:
        headers: Dict = self.__headers["create_invoice"]
        headers["ApiUserCompanyRoleKey"] = headers["ApiUserCompanyRoleKey"].replace("{ing_api_key}", self.__credentials["ing_api_key"])
        return headers

    def get_invoice(self) -> Dict:
        headers: Dict = self.__headers["get_invoice"]
        headers["ApiUserCompanyRoleKey"] = headers["ApiUserCompanyRoleKey"].replace("{ing_api_key}", self.__credentials["ing_api_key"])
        return headers