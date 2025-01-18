import requests
from jsonschema import validate
import json
import allure
from utils.attach import response_attaching, response_logging
from utils.path_file import get_dir
from datetime import datetime

SCHEMA_FILE_DIR = get_dir("schemas")


@allure.epic("Reqres API")
@allure.feature("/{resource}/{id}")
@allure.story("PUT")
@allure.tag("API")
@allure.label("owner", "Gleb T")
@allure.title("Проверка изменения данных ресурса")
@allure.severity(allure.severity_level.CRITICAL)
def test_put_resource_success_validation_schema(base_url):

    with allure.step('Отправляем запрос на изменение данных ресурса'):
        response = requests.put(base_url + '/{resource}/{id}')
        response_attaching(response)
        response_logging(response)

    with allure.step('Проверяем статус-код'):
        assert response.status_code == 200
        data = response.json()

    with allure.step('Проверяем схему'):
        with open(f"{SCHEMA_FILE_DIR}/put_resource.json") as file:
            validate(instance=data, schema=json.load(file))

    with allure.step('Проверяем значение response'):
        assert 'updatedAt' in data
        updated_at_value = data['updatedAt']
        date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        try:
            datetime.strptime(updated_at_value, date_format)
        except ValueError:
            raise AssertionError("Значение поля 'updatedAt' имеет неправильный формат.")
