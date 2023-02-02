import json

import pytest

from api_framework.src.config.base_url import BaseUrl
from api_framework.src.utilities.endpoints import Endpoints
from api_framework.src.utilities.json_files_path import JsonFilesPath
from api_framework.src.utilities.read_json_file import ReadJsonFile


# class TestAllRequest(object):
#
#     def __int__(self):
base_url = BaseUrl()
read_json_file = ReadJsonFile()
endpoint = Endpoints()
json_files_path = JsonFilesPath()

final_post_url = base_url.fake_rest_api_domain + endpoint.fake_rest_api_endpoint


@pytest.mark.parametrize("test", read_json_file.post_method(json_files_path.fake_rest_api, json_files_path.fake_rest_api_object_name, final_post_url, base_url.headers))
def test_post_request(test):
    assert test.status_code == 200
    data = test.json()
    #assert data["completed"] == False
    print(data)
    global id
    id = data["id"]


def test_get_request():
    final_url = final_post_url + f'/{id}'
    print(final_url)
    response = read_json_file.get_method(final_url, base_url.headers)
    assert response.status_code == 200
    json_body = response.json()
    print(json_body)


def test_put_request():
    final_url = final_post_url + "/" + f'{id}'
    update_payload = {"sal": 25000, "designation": "Engineer"}
    response = read_json_file.put_mehtod(json_files_path.fake_rest_api, json_files_path.fake_rest_api_object_name, final_url, update_payload, id, base_url.headers)
    print(response)
    data = response.json()
    print(data)


# def test_delete_object_put_request():
#     final_url = final_post_url + "/" +f'{id}'
#     delete_payload = {"sal" : 25000}
#     response = read_json_file.remove_object_put_method(json_files_path.fake_rest_api, json_files_path.fake_rest_api_object_name, final_url, delete_payload, id, base_url.headers)
#     print(response)

def test_delete_request():
    final_url = final_post_url + "/" +f'{id}'
    response = read_json_file.delete_method(final_url)
    print(response)
