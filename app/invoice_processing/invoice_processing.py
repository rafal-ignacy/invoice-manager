from dataclasses import dataclass

from app.database.invoice_db_operations import InvoiceDatabaseOperations


@dataclass
class InvoiceProcessing:
    def get_orders_data_for_creating_invoices(self):
        invoice_database_operations = InvoiceDatabaseOperations()
        self.orders_list = invoice_database_operations.get_details_of_paid_orders_without_invoice()
        for order in self.orders_list:
            ORDER_DETAILS, ORDER_ID, CUSTOMER_ID = 0, 0, 4
            order.append(invoice_database_operations.get_customer_details(order[ORDER_DETAILS][CUSTOMER_ID]))
            order.append(invoice_database_operations.get_items_details(order[ORDER_DETAILS][ORDER_ID]))

    def check_sku_existence_in_orders_items(self):
        SKU, ITEMS_DETAILS = 0, 2
        for order_index in range(len(self.orders_list) - 1, -1, -1):
            for item in self.orders_list[order_index][ITEMS_DETAILS]:
                if item[SKU] is None:
                    self.orders_list.pop(order_index)
                    break
        print(self.orders_list)
