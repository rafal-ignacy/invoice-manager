import json


from app.web_requests.request_component import RequestComponent
from app.settings import ROOT_DIR


def test_get_file_data_dict():
    request_component = RequestComponent()
    with open(ROOT_DIR + "/tests/data/request_components.json") as data_file:
        file_data_dict = json.loads(data_file.read())
    assert file_data_dict == request_component.get_file_data_dict(ROOT_DIR + "/tests/data/request_components.json")
