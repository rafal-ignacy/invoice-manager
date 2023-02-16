from dataclasses import dataclass
from typing import List, Tuple, Dict

from app.data_models.invoice.invoice_details import InvoiceDetails
from app.data_models.invoice.customer_details import CustomerDetails
from app.data_models.invoice.item_details import ItemDetails
from app.invoice_processing.invoice_data_processing import InvoiceDataProcessing


@dataclass
class InvoiceDataHandler:
    def __init__(self):
        self.invoice_data_processing = InvoiceDataProcessing()

    def get_invoice_object(self, order: List) -> InvoiceDetails:
        ORDER_DETAILS, CUSTOMER_DETAILS, ITEMS_DETAILS, SHIPPING_PRICE = 0, 1, 2, 4
        invoice_details_dict = self.invoice_data_processing.get_invoice_details_dict(order[ORDER_DETAILS])
        customer_details: CustomerDetails = self.get_customer_details(order[CUSTOMER_DETAILS])
        items_details: List[ItemDetails] = self.get_items_details(order[ITEMS_DETAILS], order[ORDER_DETAILS][SHIPPING_PRICE])
        return InvoiceDetails(invoice_details_dict["issue_date"], invoice_details_dict["service_date"],
                              invoice_details_dict["currency"], invoice_details_dict["paid_amount"],
                              invoice_details_dict["rate"], customer_details, items_details)

    def get_customer_details(self, customer_details: Tuple) -> CustomerDetails:
        customer_details_dict: Dict = self.invoice_data_processing.get_invoice_customer_details_dict(customer_details)
        return CustomerDetails(customer_details_dict["email"], customer_details_dict["full_name"],
                               customer_details_dict["address_street"], customer_details_dict["city"],
                               customer_details_dict["post_code"], customer_details_dict["country_code"],
                               customer_details_dict["tax_country_code"])

    def get_items_details(self, items_details: List, shipping_price: float) -> List[ItemDetails]:
        items_details_list_objects: List[ItemDetails] = []
        for item_details in items_details:
            item_details_dict = self.invoice_data_processing.get_invoice_item_details_dict(item_details)
            items_details_list_objects.append(ItemDetails(item_details_dict["name"], item_details_dict["code"],
                                                          item_details_dict["quantity"], item_details_dict["price"]))
        shipping_details_dict: Dict = self.invoice_data_processing.get_shipping_details_dict(shipping_price)
        items_details_list_objects.append(ItemDetails(shipping_details_dict["name"], shipping_details_dict["code"],
                                                      shipping_details_dict["quantity"], shipping_details_dict["price"]))
        return items_details_list_objects
