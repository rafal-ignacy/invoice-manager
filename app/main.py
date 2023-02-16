from app.utils.date_handler import DateHandler
from app.web_requests.web_requests import WebRequests
from app.utils.response_handler import ResponseHandler
from app.orders_processing.orders_processing import OrdersProcessing
from app.invoice_processing.invoice_processing import InvoiceProcessing
from app.utils.mail_handler import MailHandler

if __name__ == "__main__":
    date_handler = DateHandler()
    utc_time = date_handler.get_orders_utc_delta(5)

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
    orders_data = invoice_processing.get_orders_data_for_creating_invoices()
    invoice_processing.check_sku_existence_in_orders_items()
    invoice_object_list = invoice_processing.create_invoice_object_list()

    invoices_binary_list = []
    for i in range(len(invoice_object_list)):
        request_response = web_requests.create_invoice(invoice_object_list[i])
        invoice_id: int = request_handler.create_invoice(request_response)
        invoice_processing.add_invoice_id_to_database(orders_data[i], invoice_id)
        invoice_binary_content: bytes = web_requests.get_invoice(invoice_id)
        invoices_binary_list.append(invoice_binary_content)

    if len(invoices_binary_list) > 0:
        mail_handler = MailHandler()
        mail_handler.send(invoices_binary_list)
