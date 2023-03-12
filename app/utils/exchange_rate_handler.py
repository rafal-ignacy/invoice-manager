from dataclasses import dataclass
from requests.exceptions import HTTPError

from app.utils.date_handler import DateHandler
from app.web_requests.web_requests import WebRequests
from app.utils.response_handler import ResponseHandler


@dataclass
class ExchangeRateHandler:
    def set_exchange_rate(self, date: str, currency: str):
        date_handler: DateHandler = DateHandler()
        web_requests = WebRequests()
        response_handler = ResponseHandler()
        exchange_rate_date: str = date_handler.set_one_day_before(date)
        while True:
            try:
                exchange_rate_response = web_requests.exchange_rate(exchange_rate_date, currency)
            except HTTPError:
                exchange_rate_date = date_handler.set_one_day_before(exchange_rate_date)
                continue
            else:
                exchance_rate = response_handler.exchange_rate(exchange_rate_response)
                return exchance_rate
