import os
import requests
from jsonschema import validate
import json

BASE_URL = 'https://reqres.in/api'


CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "..", "schemas")


def test_get_user_success_validation_schema():
    response = requests.get(f'{BASE_URL}/users/2')

    if response.status_code == 200:
        data = response.json()

        with open(f"{FILE}/get_user.json") as file:
            validate(instance=data, schema=json.load(file))


def test_get_user_not_found_error_code():
    response = requests.get(f'{BASE_URL}/users/2940381')

    assert response.status_code == 404
