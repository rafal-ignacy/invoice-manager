from dataclasses import dataclass
from typing import Tuple

from app.database.db import Database
from app.data_models.order.customer_details import CustomerDetails
from app.data_models.order.order_details import OrderDetails
from app.data_models.order.item_details import ItemDetails
from app.database.db_operations import DatabaseOperations


@dataclass
class OrdersDatabaseOperations(DatabaseOperations):
    def __init__(self):
        self.queries_data = self.get_queries_data()

    def check_order_existence_in_database(self, platform_order_id: str | int) -> bool:
        SQL_query: str = self.queries_data["check_order_existence_in_database"].replace("{platform_order_id}", str(platform_order_id))
        with Database(function_name="Check order existence in database") as database:
            database.cursor.execute(SQL_query)
            result = database.cursor.fetchall()[0][0]
        if result > 0:
            return True
        else:
            return False

    def add_customer_details(self, customer_details: CustomerDetails) -> int:
        SQL_query: str = self.queries_data["add_customer_details"]
        SQL_values: Tuple = tuple(customer_details.__dict__.values())
        with Database(function_name="Add customer details") as database:
            database.cursor.execute(SQL_query, SQL_values)
            database.commit()
            customer_id: int = database.cursor.lastrowid
        return customer_id

    def add_order_details(self, order_details: OrderDetails, customer_id: int):
        SQL_query: str = self.queries_data["add_order_details"]
        SQL_values_list = list(order_details.__dict__.values())[:-2]
        SQL_values_list.append(customer_id)
        SQL_values_tuple = tuple(SQL_values_list)
        with Database(function_name="Add order details") as database:
            database.cursor.execute(SQL_query, SQL_values_tuple)
            database.commit()
            order_id: int = database.cursor.lastrowid
        return order_id

    def add_item_details(self, item_details: ItemDetails, order_id: int):
        SQL_query: str = self.queries_data["add_item_details"]
        SQL_values_list = list(item_details.__dict__.values())
        SQL_values_list.append(order_id)
        SQL_values_tuple = tuple(SQL_values_list)
        with Database(function_name="Add item details") as database:
            database.cursor.execute(SQL_query, SQL_values_tuple)
            database.commit()
