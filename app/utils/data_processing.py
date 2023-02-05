from dataclasses import dataclass
from typing import List, Tuple

from app.data_models.order.item_details import ItemDetails
from app.utils.date_handler import DateHandler


@dataclass
class DataProcessing:
    def convert_dates(self, order_date: str, payment_date: str | None):
        date_handler: DateHandler = DateHandler()
        order_date = date_handler.convert_date(order_date[:-5])
        if payment_date is not None:
            payment_date = date_handler.convert_date(payment_date[:-5])
        return order_date, payment_date

    def convert_types(self, total: str | float, delivery_total: str | float, items_list: List[ItemDetails]) -> Tuple[float, float]:
        total, delivery_total = float(total), float(delivery_total)
        for item in items_list:
            item.price = float(item.price)
        return total, delivery_total

    def convert_sku(self, items_list: List[ItemDetails]):
        for item in items_list:
            if item.sku is not None:
                item.sku = item.sku[:-3]
