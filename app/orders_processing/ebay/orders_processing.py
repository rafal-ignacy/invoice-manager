from dataclasses import dataclass
from typing import List

from app.database.orders_db_operations import OrdersDatabaseOperations
from app.utils.data_processing import DataProcessing
from app.orders_processing.ebay.ebay_order_data_handler import EbayOrderDataHandler
from app.orders_processing.order_processing import OrderProcessing


@dataclass
class EbayOrdersProcessing(OrderProcessing):
    def __init__(self):
        self.orders_list = []
        self.database_operations = OrdersDatabaseOperations()

    def get_orders_data(self, ebay_orders_list: List):
        order_data_handler = EbayOrderDataHandler()
        for ebay_order in ebay_orders_list:
            self.orders_list.append(order_data_handler.get_details(ebay_order))
        self.orders_list.reverse()

    def prepare_orders_data_to_database(self):
        data_processing = DataProcessing()
        for order in self.orders_list:
            order.order_date, order.payment_date = data_processing.convert_dates(order.order_date, order.payment_date)
            order.total, order.delivery_total = data_processing.convert_types(order.total, order.delivery_total, order.items_details)
            data_processing.convert_sku(order.items_details)
