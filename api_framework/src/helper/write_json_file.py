import json
import os

from api_framework.src.helper.create_payload import CreatePayload

# from api_framework.src.config.base_url import BaseUrl
# from api_framework.src.utilities.endpoints import Endpoints
#
# base_url = BaseUrl()
# endpoint = Endpoints()
#
# fake_rest_api = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..', 'test','test_data', 'fake_rest_api_test_data.json'))
# object_name = "test_data"
# final_post_url = base_url.domain + endpoint.fake_rest_api_endpoint + "/1"
# updated_payload = {"dueDate": "2023-01-15T16:54:54.883Z"}
# added_payload = {"designation":"Engineer"}


class WriteJsonFile(object):

    def __init__(self):
        self.dictobj = []
        self.add_multi_element = {}
        self.delete_payload = {}
        self.create_payload = CreatePayload()

    def read_data_from_json_file(self, payload, object_name):
        with open(payload) as json_file:
            self.dictobj = json.load(json_file)
        for i in self.dictobj[object_name]:
            i.update({"title": f"{self.create_payload.create_title()}"})
            with open(payload, "w", encoding='utf-8') as json_file:
                json.dump(self.dictobj, json_file, indent=4)
        json_file = json.dumps(self.dictobj)
        return json_file

    def update_payload(self, payload, object_name, body_id, update_payload=None):
        json_file = self.read_data_from_json_file(payload, object_name)
        file = json.loads(json_file)
        for self.add_multi_element in file[object_name]:
            if self.add_multi_element["id"] == body_id:
                self.add_multi_element.update(update_payload)
                with open(payload, "w", encoding='utf-8') as json_file:
                    json.dump(file, json_file,indent=4)
        return self.add_multi_element
        #print(i)

    def delete_payload(self, payload, object_names, body_id, delete_payload=None):
        json_file = self.read_data_from_json_file(payload, object_names)
        file = json.loads(json_file)
        for self.delete_payload in file[object_names]:
            if self.delete_payload["id"] == body_id:
               self.delete_payload.pop(delete_payload)
               with open(payload, "w", encoding='utf-8') as json_file:
                    json.dump(file, json_file, indent=4)
        return self.delete_payload


# write = WriteJsonFile()
# write.update_payload(fake_rest_api, object_name, 1, added_payload)
#write.read_data_from_json_file(fake_rest_api, object_name)
# write.add_payload(fake_rest_api, object_name, 1, added_payload)
