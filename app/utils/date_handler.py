from datetime import datetime, timedelta


class DateHandler:
    def get_orders_utc_delta(self, hour_difference) -> str:
        utc_now = datetime.utcnow()
        utc_subtracted = utc_now - timedelta(hours=hour_difference)
        return utc_subtracted.strftime("%Y-%m-%dT%H:%M:%S.000Z")
