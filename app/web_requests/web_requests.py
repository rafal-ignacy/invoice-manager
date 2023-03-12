from dataclasses import dataclass
from typing import Dict
from requests import HTTPError

from app.web_requests.web_request import WebRequest
from app.web_requests.urls import Urls
from app.web_requests.headers import Headers
from app.web_requests.payloads import Payloads
from app.utils.logger import Logger
from app.data_models.invoice.invoice_details import InvoiceDetails


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

    def get_ebay_orders(self, date: str, access_token: str) -> Dict:
        url: str = self.urls.get_ebay_orders(date)
        headers: Dict = self.headers.get_ebay_orders(access_token)
        request: WebRequest = WebRequest(url, headers)
        response: Dict = self.execute_request(request, "eBay get orders")
        return response

    def get_ebay_order(self, order_id: str, access_token: str) -> Dict:
        url: str = self.urls.get_ebay_order(order_id)
        headers: Dict = self.headers.get_ebay_order(access_token)
        request: WebRequest = WebRequest(url, headers)
        response: Dict = self.execute_request(request, "eBay get order")
        return response

    def create_invoice(self, invoice_details: InvoiceDetails) -> Dict:
        url: str = self.urls.create_invoice()
        headers: Dict = self.headers.create_invoice()
        payload: Dict = self.payloads.create_invoice(invoice_details)
        request: WebRequest = WebRequest(url, headers, payload)
        print(payload)
        response: Dict = self.execute_request(request, "ING API create invoice")
        return response

    def get_invoice(self, invoice_id: int) -> bytes:
        url: str = self.urls.get_invoice(str(invoice_id))
        headers: Dict = self.headers.get_invoice()
        request: WebRequest = WebRequest(url, headers)
        response: bytes = self.execute_request(request, "ING API get invoice")
        return response

    def exchange_rate(self, date: str, currency: str) -> Dict:
        url: str = self.urls.exchange_rate(date, currency)
        request: WebRequest = WebRequest(url)
        response: Dict = self.execute_request(request, "NBP API exchange rate")
        return response

    def get_etsy_access_token(self) -> Dict:
        url: str = self.urls.get_etsy_access_token()
        headers: Dict = self.headers.get_etsy_access_token()
        payload: Dict = self.payloads.get_etsy_access_token()
        request: WebRequest = WebRequest(url, headers, payload)
        response: Dict = self.execute_request(request, "Etsy get access token")
        return response

    def get_etsy_orders(self, timestamp: int, access_token: str) -> Dict:
        url: str = self.urls.get_etsy_orders(timestamp)
        headers: Dict = self.headers.get_etsy_orders(access_token)
        request: WebRequest = WebRequest(url, headers)
        response: Dict = self.execute_request(request, "Etsy get orders")
        return response

    def execute_request(self, request, message):
        try:
            response = request.response()
            self.logger.info(message)
        except HTTPError:
            self.logger.error(message)
            raise HTTPError
        return response
