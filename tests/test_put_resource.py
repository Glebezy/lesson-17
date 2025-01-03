import os
import requests
from jsonschema import validate
import json

BASE_URL = 'https://reqres.in/api'

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "..", "schemas")


def test_put_resource_success_validation_schema():
    response = requests.put(BASE_URL + '/{resource}/{id}')

    if response.status_code == 200:
        data = response.json()

        with open(f"{FILE}/put_resource.json") as file:
            validate(instance=data, schema=json.load(file))
