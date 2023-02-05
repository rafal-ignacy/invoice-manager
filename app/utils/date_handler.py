from datetime import datetime, timedelta


class DateHandler:
    def get_orders_utc_delta(self, hour_difference: int) -> str:
        utc_now: datetime = datetime.utcnow()
        utc_subtracted: datetime = utc_now - timedelta(hours=hour_difference)
        return utc_subtracted.strftime("%Y-%m-%dT%H:%M:%S.000Z")

    def convert_date(self, date: str) -> str:
        datetime_object: datetime = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        datetime_converted: str = datetime.strftime(datetime_object, "%d/%m/%Y %H:%M:%S")
        return datetime_converted
