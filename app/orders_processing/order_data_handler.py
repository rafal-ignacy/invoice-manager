from dataclasses import dataclass
from typing import Dict, List
import json
import flatten_json  # type: ignore

from app.data_models.order.customer_details import CustomerDetails
from app.data_models.order.order_details import OrderDetails
from app.data_models.order.item_details import ItemDetails


@dataclass
class OrderDataHandler:
    def get_config(self, path) -> Dict:
        with open(path, "r") as json_file:
            json_data = json.loads(json_file.read())
        return json_data

    def get_details(self, order_dict: Dict) -> OrderDetails:
        order_dict_flatten: Dict = flatten_json.flatten(order_dict)
        customer_details: CustomerDetails = self.get_customer_details(order_dict_flatten, self.config_data)  # type: ignore
        items_details: List[ItemDetails] = self.get_items_details(order_dict_flatten)  # type: ignore
        order_details: OrderDetails = self.get_order_details(order_dict_flatten, customer_details, items_details)  # type: ignore
        return order_details

    def get_customer_details(self, order_dict_flatten: Dict, config_data: Dict) -> CustomerDetails:
        object_dict: Dict = {key: order_dict_flatten.get(value) for (key, value) in config_data["get_customer_details"].items()}

        return CustomerDetails(object_dict["email"], object_dict["username"], object_dict["full_name"],
                               object_dict["address_line1"], object_dict["address_line2"], object_dict["city"],
                               object_dict["post_code"], object_dict["state_or_province"], object_dict["country_code"])
