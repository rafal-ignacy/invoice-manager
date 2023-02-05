from dataclasses import dataclass


@dataclass
class OrderDetails:
    order_ebay_id: str
    platform: str
    order_date: str
    currency: str
    payment_date: str | None
    payment_status: str
    total: str | float
    delivery_total: str | float
