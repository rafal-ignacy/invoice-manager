from dataclasses import dataclass
from typing import List

from app.database.orders_db_operations import OrdersDatabaseOperations
from app.utils.data_processing import DataProcessing
from app.orders_processing.order_data_handler import OrderDataHandler

ORDER_DETAILS = 0
CUSTOMER_DETAILS = 1
ITEMS_DETAILS = 2


@dataclass
class OrdersProcessing:
    def __init__(self):
        self.orders_list = []
        self.database_operations = OrdersDatabaseOperations()

    def get_orders_data(self, ebay_orders_list: List):
        order_data_handler = OrderDataHandler()
        for ebay_order in ebay_orders_list:
            self.orders_list.append(order_data_handler.get_details(ebay_order))
        self.orders_list.reverse()

    def check_orders_existence_in_database(self) -> None:
        for order_index in range(len(self.orders_list) - 1, -1, -1):
            order_ebay_id: str = self.orders_list[order_index][ORDER_DETAILS].order_ebay_id  # type: ignore
            result = self.database_operations.check_order_existence_in_database(order_ebay_id)
            if result is True:
                self.orders_list.pop(order_index)

    def prepare_orders_data_to_database(self):
        data_processing = DataProcessing()
        for order in self.orders_list:
            order_details = order[ORDER_DETAILS]
            item_details = order[ITEMS_DETAILS]
            order_details.order_date, order_details.payment_date = data_processing.convert_dates(order_details.order_date, order_details.payment_date)
            order_details.total, order_details.delivery_total = data_processing.convert_types(order_details.total, order_details.delivery_total, item_details)
            data_processing.convert_sku(item_details)

    def add_orders_to_database(self):
        for order in self.orders_list:
            customer_id = self.database_operations.add_customer_details(order[CUSTOMER_DETAILS])
            order_id = self.database_operations.add_order_details(order[ORDER_DETAILS], customer_id)
            for item_details in order[ITEMS_DETAILS]:
                self.database_operations.add_item_details(item_details, order_id)
