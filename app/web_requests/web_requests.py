from dataclasses import dataclass
from typing import Dict
from requests import HTTPError

from app.web_requests.web_request import WebRequest
from app.web_requests.urls import Urls
from app.web_requests.headers import Headers
from app.web_requests.payloads import Payloads
from app.utils.logger import Logger


@dataclass
class WebRequests:
    def __init__(self):
        self.urls = Urls()
        self.headers = Headers()
        self.payloads = Payloads()
        self.logger = Logger()

    def get_ebay_access_token(self) -> Dict:
        url: str = self.urls.get_ebay_access_token()
        headers: Dict = self.headers.get_ebay_access_token()
        payload: Dict = self.payloads.get_ebay_access_token()
        request: WebRequest = WebRequest(url, headers, payload)
        response: Dict = self.execute_request(request, "eBay get access token")
        return response

    def get_orders(self, date: str, access_token: str) -> Dict:
        url: str = self.urls.get_orders(date)
        headers: Dict = self.headers.get_orders(access_token)
        request: WebRequest = WebRequest(url, headers)
        response: Dict = self.execute_request(request, "eBay get orders")
        return response

    def get_order(self, order_id: str, access_token: str) -> Dict:
        url: str = self.urls.get_order(order_id)
        headers: Dict = self.headers.get_order(access_token)
        request: WebRequest = WebRequest(url, headers)
        response: Dict = self.execute_request(request, "eBay get order")
        return response

    def create_invoice(self, order_data: Dict) -> Dict:
        url: str = self.urls.create_invoice()
        headers: Dict = self.headers.create_invoice()
        payload: Dict = self.payloads.create_invoice(order_data)
        request: WebRequest = WebRequest(url, headers, payload)
        response: Dict = self.execute_request(request, "ING API create invoice")
        return response

    def execute_request(self, request, message) -> Dict:
        try:
            response: Dict = request.response()
            self.logger.info(message)
        except HTTPError:
            self.logger.error(message)
            raise HTTPError
        return response
