from dataclasses import dataclass
from typing import Dict, List

from app.settings import ROOT_DIR
from app.orders_processing.order_data_handler import OrderDataHandler
from app.data_models.order.order_details import OrderDetails
from app.data_models.order.customer_details import CustomerDetails
from app.data_models.order.item_details import ItemDetails
from app.utils.data_processing import DataProcessing
from app.utils.data_processing import DateHandler


@dataclass
class EtsyOrderDataHandler(OrderDataHandler):
    def __init__(self) -> None:
        self.config_data: Dict = self.get_config(ROOT_DIR + r"/app/data/order_data_handler.json")["etsy"]

    def get_order_details(self, order_dict_flatten: Dict, customer_details: CustomerDetails, items_details: List[ItemDetails]) -> OrderDetails:
        object_dict: Dict = {key: order_dict_flatten.get(value) for (key, value) in self.config_data["get_order_details"].items()}

        data_processing = DataProcessing()
        date_handler = DateHandler()
        object_dict["platform"] = self.config_data["platform"]
        object_dict["delivery_total"] = object_dict["delivery_total"] / object_dict["delivery_total_divisor"]
        object_dict["total"] = object_dict["total"] / object_dict["total_divisor"] + object_dict["delivery_total"]
        object_dict["payment_status"] = data_processing.uppercase_payment_status(object_dict["payment_status"])
        object_dict["order_date"] = date_handler.convert_date_from_timestamp(object_dict["order_date"])
        object_dict["payment_date"] = date_handler.convert_date_from_timestamp(object_dict["payment_date"])

        return OrderDetails(object_dict["order_etsy_id"], object_dict["platform"],
                            object_dict["order_date"], object_dict["currency"],
                            object_dict["payment_date"], object_dict["payment_status"],
                            object_dict["total"], object_dict["delivery_total"],
                            customer_details, items_details)

    def get_items_details(self, order_dict_flatten: Dict) -> List[ItemDetails]:
        items_list: List[ItemDetails] = []
        item_index: int | None = 0
        while item_index is not None:
            object_dict: Dict = {}
            for key, value in self.config_data["get_items_details"].items():
                object_dict_key = value.replace("{id}", str(item_index))
                if order_dict_flatten.get(object_dict_key) is None and key != "sku":
                    item_index = None
                    break
                object_dict[key] = order_dict_flatten.get(object_dict_key)
            if item_index is not None:
                object_dict["price"] = object_dict["price"] / object_dict["price_divisor"]
                items_list.append(ItemDetails(object_dict["item_etsy_id"], object_dict["sku"], object_dict["quantity"], object_dict["price"]))
                item_index += 1
        return items_list
