from dataclasses import dataclass


from app.settings import ROOT_DIR
from app.web_requests.request_component import RequestComponent


@dataclass
class Urls(RequestComponent):
    def __init__(self) -> None:
        self.__urls = self.get_file_data_dict(ROOT_DIR + r"\app\data\urls.json")

    def get_ebay_access_token(self) -> str:
        url: str = self.__urls["get_ebay_access_token"]
        return url

    def get_order(self, order_id: str) -> str:
        url: str = self.__urls["get_order"].replace("{order_id}", order_id)
        return url

    def get_orders(self, date: str) -> str:
        url: str = self.__urls["get_orders"].replace("{date}", date)
        return url

    def create_invoice(self) -> str:
        url: str = self.__urls["create_invoice"]
        return url
