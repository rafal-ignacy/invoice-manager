import time

from app.utils.date_handler import DateHandler
from app.web_requests.web_requests import WebRequests
from app.utils.response_handler import ResponseHandler
from app.utils.mail_handler import MailHandler
from app.utils.etsy_refresh_token_handler import EtsyRefreshTokenHandler
from app.orders_processing.ebay.orders_processing import EbayOrdersProcessing
from app.orders_processing.etsy.orders_processing import EtsyOrdersProcessing
from app.invoice_processing.invoice_processing import InvoiceProcessing


if __name__ == "__main__":
    while True:
        date_handler = DateHandler()
        web_requests = WebRequests()
        request_handler = ResponseHandler()
        etsy_refresh_token_handler = EtsyRefreshTokenHandler()

        etsy_access_token_response = web_requests.get_etsy_access_token()
        access_token = request_handler.get_etsy_access_token(etsy_access_token_response)
        refresh_token = request_handler.get_etsy_refresh_token(etsy_access_token_response)
        etsy_refresh_token_handler.save_refresh_token(refresh_token)

        timestamp = date_handler.get_orders_utc_delta_timestamp(1)
        request_response = web_requests.get_etsy_orders(timestamp, access_token)
        etsy_orders_list = request_handler.get_etsy_orders(request_response)

        print(etsy_orders_list)

        etsy_orders_processing = EtsyOrdersProcessing()
        etsy_orders_processing.get_orders_data(etsy_orders_list)
        etsy_orders_processing.check_orders_existence_in_database()
        etsy_orders_processing.prepare_orders_data_to_database()
        etsy_orders_processing.add_orders_to_database()

        ebay_access_token_response = web_requests.get_ebay_access_token()
        ebay_access_token = request_handler.get_ebay_access_token(ebay_access_token_response)

        utc_time = date_handler.get_orders_utc_delta(1)
        request_response = web_requests.get_ebay_orders(utc_time, ebay_access_token)
        ebay_orders_list = request_handler.get_ebay_orders(request_response)

        print(ebay_orders_list)

        ebay_orders_processing = EbayOrdersProcessing()
        ebay_orders_processing.get_orders_data(ebay_orders_list)
        ebay_orders_processing.check_orders_existence_in_database()
        ebay_orders_processing.prepare_orders_data_to_database()
        ebay_orders_processing.add_orders_to_database()

        invoice_processing = InvoiceProcessing()
        orders_data = invoice_processing.get_orders_data_for_creating_invoices()

        print(orders_data)

        invoice_processing.check_sku_existence_in_orders_items()
        invoice_object_list = invoice_processing.create_invoice_object_list()

        print(invoice_object_list)

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
        invoices_amount: int = len(invoices_binary_list)
        print(f"Sent {invoices_amount} invoices")

        time.sleep(600)
