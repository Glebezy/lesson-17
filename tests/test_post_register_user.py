import os
import requests
from jsonschema import validate
import json
import allure
from utils.attach import response_attaching, response_logging
from utils.file import get_dir

SCHEMA_FILE_DIR = get_dir("schemas")
MODEL_FILE_DIR = get_dir("models")

USER_CREDS = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}


@allure.epic("Reqres API")
@allure.feature("/register")
@allure.story("POST")
@allure.tag("API")
@allure.label("owner", "Gleb T")
class TestPostRegisterUser:

    @allure.title("Проверка регистрации пользователя с валидными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_post_register_success_validation_schema(self, base_url):

        with allure.step('Отправляем запрос на регистрацию с валидными данными'):
            response = requests.post(f'{base_url}/register', USER_CREDS)
            response_attaching(response)
            response_logging(response)

        with allure.step('Проверяем статус-код'):
            assert response.status_code == 200
            data = response.json()

        with allure.step('Проверяем схему'):
            with open(f"{SCHEMA_FILE_DIR}/post_register.json") as file:
                validate(instance=data, schema=json.load(file))

        with allure.step('Проверяем значение response'):
            with open(f"{MODEL_FILE_DIR}/user.json", 'r') as file:
                assert data == json.load(file)['register_info']

    @allure.title("Проверка регистрации пользователя с невалидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_post_register_failure_validation_schema(self, base_url):

        with allure.step('Отправляем запрос на регистрацию с невалидными данными'):
            response = requests.post(f'{base_url}/register', USER_CREDS['email'])
            response_attaching(response)
            response_logging(response)

        with allure.step('Проверяем статус-код'):
            assert response.status_code == 400
            data = response.json()

        with allure.step('Проверяем схему'):
            with open(f"{SCHEMA_FILE_DIR}/post_register_error.json") as file:
                validate(instance=data, schema=json.load(file))
