from dataclasses import dataclass
from typing import List

from app.data_models.order.customer_details import CustomerDetails
from app.data_models.order.item_details import ItemDetails


@dataclass
class OrderDetails:
    platform_order_id: str
    platform: str
    order_date: str
    currency: str
    payment_date: str | None
    payment_status: str
    total: str | float
    delivery_total: str | float
    customer_details: CustomerDetails
    items_details: List[ItemDetails]
