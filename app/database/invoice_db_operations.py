from typing import List
from dataclasses import dataclass

from app.database.db import Database
from app.database.db_operations import DatabaseOperations


@dataclass
class InvoiceDatabaseOperations(DatabaseOperations):
    def __init__(self) -> None:
        self.queries_data = self.get_queries_data()

    def get_details_of_paid_orders_without_invoice(self) -> List:
        SQL_query: str = self.queries_data["get_details_of_paid_orders_without_invoice"]
        with Database(function_name="Get details of paid orders without invoice") as database:
            database.cursor.execute(SQL_query)
            database_result: List = database.cursor.fetchall()

        orders_list = []
        for database_order_data in database_result:
            order_details = []
            order_details.append(database_order_data)
            orders_list.append(order_details)
        return orders_list

    def get_customer_details(self, customer_id: int):
        SQL_query: str = self.queries_data["get_customer_details"].replace("{customer_id}", str(customer_id))
        with Database(function_name="Get customer details") as database:
            database.cursor.execute(SQL_query)
            result: List = database.cursor.fetchall()[0]
        return result

    def get_items_details(self, order_id: int):
        SQL_query: str = self.queries_data["get_items_details"].replace("{order_id}", str(order_id))
        with Database(function_name="Get items details") as database:
            database.cursor.execute(SQL_query)
            result: List = database.cursor.fetchall()
        return result

    def add_invoice_id(self, order_id: int, invoice_id: int):
        SQL_query: str = self.queries_data["add_invoice_id"].replace("{order_id}", str(order_id))
        SQL_query = SQL_query.replace("{invoice_id}", str(invoice_id))
        with Database(function_name="Add invoice ID") as database:
            database.cursor.execute(SQL_query)
            database.commit()
