from dataclasses import dataclass
from typing import List, Any

from app.database.invoice_db_operations import InvoiceDatabaseOperations
from app.invoice_processing.invoice_data_handler import InvoiceDataHandler


@dataclass
class InvoiceProcessing:
    def get_orders_data_for_creating_invoices(self):
        self.invoice_database_operations = InvoiceDatabaseOperations()
        self.orders_list: List[Any] = self.invoice_database_operations.get_details_of_paid_orders_without_invoice()  # type: ignore
        for order in self.orders_list:
            ORDER_DETAILS, ORDER_ID, CUSTOMER_ID = 0, 0, 5
            order.append(self.invoice_database_operations.get_customer_details(order[ORDER_DETAILS][CUSTOMER_ID]))
            order.append(self.invoice_database_operations.get_items_details(order[ORDER_DETAILS][ORDER_ID]))
        return self.orders_list

    def check_sku_existence_in_orders_items(self):
        SKU, ITEMS_DETAILS = 0, 2
        for order_index in range(len(self.orders_list) - 1, -1, -1):
            for item in self.orders_list[order_index][ITEMS_DETAILS]:
                if item[SKU] is None:
                    self.orders_list.pop(order_index)
                    break

    def create_invoice_object_list(self):
        invoice_object_list = []
        invoice_data_handler = InvoiceDataHandler()
        for order in self.orders_list:
            invoice_object_list.append(invoice_data_handler.get_invoice_object(order))
        return invoice_object_list

    def add_invoice_id_to_database(self, order_details: List, invoice_id: int):
        ORDER_DETAILS, ORDER_ID = 0, 0
        self.invoice_database_operations.add_invoice_id(order_details[ORDER_DETAILS][ORDER_ID], invoice_id)
