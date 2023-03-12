from dataclasses import dataclass
from typing import List

from app.orders_processing.etsy.etsy_order_data_handler import EtsyOrderDataHandler
from app.orders_processing.order_processing import OrderProcessing
from app.database.orders_db_operations import OrdersDatabaseOperations
from app.utils.data_processing import DataProcessing


@dataclass
class EtsyOrdersProcessing(OrderProcessing):
    def __init__(self):
        self.orders_list = []
        self.database_operations = OrdersDatabaseOperations()

    def get_orders_data(self, etsy_orders_list: List):
        order_data_handler = EtsyOrderDataHandler()
        for etsy_order in etsy_orders_list:
            self.orders_list.append(order_data_handler.get_details(etsy_order))
        self.orders_list.reverse()

    def prepare_orders_data_to_database(self):
        data_processing = DataProcessing()
        for order in self.orders_list:
            data_processing.convert_sku(order.items_details)
