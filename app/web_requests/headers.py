from dataclasses import dataclass
from typing import Dict
import json


from app.settings import ROOT_DIR


@dataclass
class Headers:
    def __init__(self) -> None:
        self.headers = self.__get_file_data_dict(ROOT_DIR + r"\app\data\headers.json")
        self.credentials: Dict = self.__get_file_data_dict(ROOT_DIR + r"\app\data\credentials.json")

    def get_ebay_access_token(self) -> Dict:
        headers: Dict = self.headers["get_ebay_access_token"]
        headers["Authorization"] = headers["Authorization"].replace("{base64_encoded_credentials}", self.credentials["ebay_base64_encoded_credentials"])
        return headers

    def get_orders(self, access_token: str) -> Dict:
        headers: Dict = self.headers["get_orders"]
        headers["Authorization"] = headers["Authorization"].replace("{ebay_access_token}", access_token)
        return headers

    def get_order(self, access_token: str) -> Dict:
        headers: Dict = self.headers["get_order"]
        headers["Authorization"] = headers["Authorization"].replace("{ebay_access_token}", access_token)
        return headers

    def create_invoice(self) -> Dict:
        headers: Dict = self.headers["create_invoice"]
        headers["ApiUserCompanyRoleKey"] = headers["ApiUserCompanyRoleKey"].replace("{ing_api_key}", self.credentials["ing_api_key"])
        return headers

    def __get_file_data_dict(self, path: str) -> Dict:
        with open(path, "r") as file:
            file_data_dict = json.loads(file.read())
        return file_data_dict
