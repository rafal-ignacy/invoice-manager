from freezegun import freeze_time


from app.utils.date_handler import DateHandler


@freeze_time("2023-01-07 00:20:34")
def test_get_orders_utc_delta():
    date_handler = DateHandler()
    result = date_handler.get_orders_utc_delta(hour_difference=2)
    print(result)
    assert result == "2023-01-06T22:20:34.000Z"
