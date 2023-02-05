from app.utils.date_handler import DateHandler
from app.web_requests.web_requests import WebRequests
from app.utils.response_handler import ResponseHandler
from app.orders_processing.orders_processing import OrdersProcessing
from app.invoice_processing.invoice_processing import InvoiceProcessing

if __name__ == "__main__":
    date_handler = DateHandler()
    utc_time = date_handler.get_orders_utc_delta(480)

    web_requests = WebRequests()
    request_handler = ResponseHandler()
    access_token_response = web_requests.get_ebay_access_token()
    access_token = request_handler.get_ebay_access_token(access_token_response)
    request_response = web_requests.get_orders(utc_time, access_token)
    ebay_orders_list = request_handler.get_orders(request_response)

    orders_processing = OrdersProcessing()
    orders_processing.get_orders_data(ebay_orders_list)
    orders_processing.check_orders_existence_in_database()
    orders_processing.prepare_orders_data_to_database()
    orders_processing.add_orders_to_database()

    invoice_processing = InvoiceProcessing()
    invoice_processing.get_orders_data_for_creating_invoices()
    invoice_processing.check_sku_existence_in_orders_items()
