import requests
import pytest


BASE_URL = 'https://reqres.in/api'


def test_delete_user_success_empty_response():
    response = requests.delete(f'{BASE_URL}/users/{id}')

    if response.status_code == 204:

        with pytest.raises(ValueError, match=r"(char 0)"):
            response.json()
