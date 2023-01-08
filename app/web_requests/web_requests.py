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
        url = self.urls.get_ebay_access_token()
        headers = self.headers.get_ebay_access_token()
        payload = self.payloads.get_ebay_access_token()
        request = WebRequest(url, headers, payload)
        try:
            response: Dict = request.response()
            self.logger.info("eBay get access token request")
        except HTTPError:
            self.logger.error("eBay get access token request")
            raise HTTPError
        return response

    def get_orders(self, date: str, access_token: str) -> Dict:
        url = self.urls.get_orders(date)
        headers = self.headers.get_orders(access_token)
        request = WebRequest(url, headers)
        try:
            response: Dict = request.response()
            self.logger.info("eBay get orders")
        except HTTPError:
            self.logger.error("eBay get orders")
            raise HTTPError
        return response

    def get_order(self, order_id: str, access_token: str) -> Dict:
        url = self.urls.get_order(order_id)
        headers = self.headers.get_order(access_token)
        request = WebRequest(url, headers)
        try:
            response: Dict = request.response()
            self.logger.info("eBay get order")
        except HTTPError:
            self.logger.error("eBay get order")
            raise HTTPError
        return response

    def create_invoice(self, order_data: Dict) -> Dict:
        url = self.urls.create_invoice()
        headers = self.headers.create_invoice()
        payload = self.payloads.create_invoice(order_data)
        request = WebRequest(url, headers, payload)
        try:
            response: Dict = request.response()
            self.logger.info("ING API create invoice - SUCCESS")
        except HTTPError:
            self.logger.error("ING API create invoice - ERROR")
            raise HTTPError
        return response
