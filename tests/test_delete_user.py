import pytest
import requests
import allure
from utils.attach import response_attaching, response_logging


@allure.epic("Reqres API")
@allure.feature("/users/{id}")
@allure.story("DELETE")
@allure.tag("API")
@allure.label("owner", "Gleb T")
@allure.title("Проверка удаления пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user_success_empty_response(base_url):

    with allure.step('Отправляем запрос на удаление пользователя'):
        response = requests.delete(f'{base_url}/users/{id}')
        response_attaching(response)
        response_logging(response)

    with allure.step('Проверяем статус-код'):
        assert response.status_code == 204

    with allure.step('Проверяем пустой ответ'):
        if response.content == b'':
            pass
        else:
            pytest.fail('Ответ не пустой.')
