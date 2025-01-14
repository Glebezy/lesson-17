import os
import requests
from jsonschema import validate
import json
import allure
from utils.attach import response_attaching, response_logging
from utils.file import get_dir

SCHEMA_FILE_DIR = get_dir("schemas")
MODEL_FILE_DIR = get_dir("models")


@allure.epic("Reqres API")
@allure.feature("/users/{id}")
@allure.story("GET")
@allure.tag("API")
@allure.label("owner", "Gleb T")
class TestGetUserById:

    @allure.title("Проверка получения данных существующего пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_success_validation_schema(self, base_url):

        with allure.step('Отправляем запрос на получение данных существующего пользователя'):
            response = requests.get(f'{base_url}/users/2')
            response_attaching(response)
            response_logging(response)

        with allure.step('Проверяем статус-код'):
            assert response.status_code == 200
            data = response.json()

        with allure.step('Проверяем схему'):
            with open(f"{SCHEMA_FILE_DIR}/get_user.json") as file:
                validate(instance=data, schema=json.load(file))

        with allure.step('Проверяем значение response'):
            with open(f"{MODEL_FILE_DIR}/user.json", 'r') as file:
                assert data == json.load(file)['get_info']

    @allure.title("Проверка получения данных несуществующего пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_not_found_error_code(self, base_url):

        with allure.step('Отправляем запрос на получение данных несуществующего пользователя'):
            response = requests.get(f'{base_url}/users/2940381')
            response_attaching(response)
            response_logging(response)

        with allure.step('Проверяем статус-код'):
            assert response.status_code == 404
