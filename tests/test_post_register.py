import os
import requests
from jsonschema import validate
import json

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "..", "schemas")

BASE_URL = 'https://reqres.in/api'

USER_CREDS = {
         "email": "eve.holt@reqres.in",
         "password": "pistol"
     }


def test_post_register_success_validation_schema():
    response = requests.post(f'{BASE_URL}/register', USER_CREDS)

    if response.status_code == 200:
        data = response.json()

        with open(f"{FILE}/post_register.json") as file:
            validate(instance=data, schema=json.load(file))


def test_post_register_failure_validation_schema():
    response = requests.post(f'{BASE_URL}/register', USER_CREDS)

    if response.status_code == 400:
        data = response.json()

        with open(f"{FILE}/post_register_error.json") as file:
            validate(instance=data, schema=json.load(file))
