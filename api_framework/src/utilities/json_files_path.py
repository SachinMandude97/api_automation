import os


class JsonFilesPath(object):

    fake_rest_api = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..', 'test','test_data', 'fake_rest_api_test_data.json'))
    fake_rest_api_object_name = "test_data"
    reqres_api = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..', 'test','test_data', 'reqres_test_data.json'))
    reqres_api_object_name = "test_data"

