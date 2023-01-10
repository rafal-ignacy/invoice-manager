from app.utils.date_handler import DateHandler
from app.web_requests.web_requests import WebRequests
from app.utils.order_data_handler import OrderDataHandler

if __name__ == "__main__":
    date_handler = DateHandler()
    utc_time = date_handler.get_orders_utc_delta(12)
    web_requests = WebRequests()
    access_token_response = web_requests.get_ebay_access_token()
    access_token = access_token_response["access_token"]
    get_order_response = web_requests.get_order("08-09558-08033", access_token)
    order_data_handler = OrderDataHandler()
    response = order_data_handler.get_details(get_order_response)
