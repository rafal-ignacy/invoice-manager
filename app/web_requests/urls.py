from dataclasses import dataclass


from app.settings import ROOT_DIR
from app.web_requests.request_component import RequestComponent


@dataclass
class Urls(RequestComponent):
    def __init__(self) -> None:
        self.__urls = self.get_file_data_dict(ROOT_DIR + r"/app/data/urls.json")
        self.__credentials = self.get_file_data_dict(ROOT_DIR + r"/app/data/credentials.json")

    def get_ebay_access_token(self) -> str:
        url: str = self.__urls["get_ebay_access_token"]
        return url

    def get_ebay_order(self, order_id: str) -> str:
        url: str = self.__urls["get_order"].replace("{order_id}", order_id)
        return url

    def get_ebay_orders(self, date: str) -> str:
        url: str = self.__urls["get_orders"].replace("{date}", date)
        return url

    def create_invoice(self) -> str:
        url: str = self.__urls["create_invoice"]
        return url

    def get_invoice(self, invoice_id: str) -> str:
        url: str = self.__urls["get_invoice"].replace("{invoice_id}", invoice_id)
        return url

    def exchange_rate(self, date: str, currency: str) -> str:
        url: str = self.__urls["exchange_rate"]
        url = url.replace("{date}", date)
        url = url.replace("{currency}", currency)
        return url

    def get_etsy_access_token(self) -> str:
        url: str = self.__urls["get_etsy_access_token"]
        return url

    def get_etsy_orders(self, timestamp: int) -> str:
        url: str = self.__urls["get_etsy_orders"]
        url = url.replace("{shop_id}", self.__credentials["etsy_shop_id"])
        url = url.replace("{timestamp}", str(timestamp))
        return url
