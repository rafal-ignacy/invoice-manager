from dataclasses import dataclass
from typing import Dict, List, Tuple
import flatten_json  # type: ignore
import json

from app.settings import ROOT_DIR
from app.data_models.order_details import OrderDetails
from app.data_models.customer_details import CustomerDetails
from app.data_models.item_details import ItemDetails


@dataclass
class OrderDataHandler:
    def __init__(self) -> None:
        self.config_data: Dict = self.get_config(ROOT_DIR + r"\app\data\order_data_handler.json")

    def get_config(self, path) -> Dict:
        with open(path, "r") as json_file:
            json_data = json.loads(json_file.read())
        return json_data

    def get_details(self, order_dict: Dict) -> Tuple[OrderDetails, CustomerDetails, List[ItemDetails]]:
        order_dict_flatten: Dict = flatten_json.flatten(order_dict)
        order_details: OrderDetails = self.get_order_details(order_dict_flatten)
        customer_details: CustomerDetails = self.get_customer_details(order_dict_flatten)
        items_details: List[ItemDetails] = self.get_items_details(order_dict_flatten)
        return order_details, customer_details, items_details

    def get_order_details(self, order_dict_flatten: Dict) -> OrderDetails:
        object_dict: Dict = {key: order_dict_flatten.get(value) for (key, value) in self.config_data["get_order_details"].items()}

        return OrderDetails(object_dict["order_ebay_id"], object_dict["platform"], object_dict["order_date"], object_dict["currency"],
                            object_dict["payment_date"], object_dict["payment_status"], object_dict["total"], object_dict["delivery_total"])

    def get_customer_details(self, order_dict_flatten) -> CustomerDetails:
        object_dict: Dict = {key: order_dict_flatten.get(value) for (key, value) in self.config_data["get_customer_details"].items()}

        return CustomerDetails(object_dict["email"], object_dict["username"], object_dict["full_name"],
                               object_dict["address_line1"], object_dict["address_line2"], object_dict["city"],
                               object_dict["post_code"], object_dict["state_or_province"], object_dict["country_code"])

    def get_items_details(self, order_dict_flatten) -> List[ItemDetails]:
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
                items_list.append(ItemDetails(object_dict["item_ebay_id"], object_dict["sku"], object_dict["quantity"], object_dict["price"]))
                item_index += 1
        return items_list
