from datetime import datetime, timedelta
import time


class DateHandler:
    def get_orders_utc_delta(self, hour_difference: int) -> str:
        utc_now: datetime = datetime.utcnow()
        utc_subtracted: datetime = utc_now - timedelta(hours=hour_difference)
        return utc_subtracted.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    def get_orders_utc_delta_timestamp(self, hour_difference: int) -> int:
        utc_now: datetime = datetime.utcnow()
        utc_subtracted: datetime = utc_now - timedelta(hours=hour_difference)
        return int(utc_subtracted.timestamp())

    def convert_date_from_ebay_format(self, date: str) -> str:
        datetime_object: datetime = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        return datetime.strftime(datetime_object, "%d/%m/%Y %H:%M:%S")

    def current_date(self) -> str:
        current_date: datetime = datetime.now()
        return datetime.strftime(current_date, "%Y-%m-%d")

    def payment_date_local_zone(self, date: str) -> str:
        now_timestamp = time.time()
        offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        datetime_object: datetime = datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
        return datetime.strftime(datetime_object + offset, "%Y-%m-%d")

    def set_one_day_before(self, date: str) -> str:
        main_date: datetime = datetime.strptime(date, "%Y-%m-%d")
        date_one_day_before: datetime = main_date - timedelta(days=1)
        return datetime.strftime(date_one_day_before, "%Y-%m-%d")

    def convert_date_from_timestamp(self, timestamp: int) -> str:
        datetime_object: datetime = datetime.fromtimestamp(timestamp)
        return datetime.strftime(datetime_object, "%d/%m/%Y %H:%M:%S")
