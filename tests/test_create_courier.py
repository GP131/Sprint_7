import pytest
import allure
import requests
from helpers import *
from data import *


class TestCreateCourier:

    @allure.title('Создать двух одинаковых курьеров')
    def test_create_duplicate_courier_fails(self, create_courier, delete_courier):
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        assert response.status_code == 409
        assert response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }

    @allure.title('Создать курьера и получить корректный ответ')
    def test_create_courier_success(self, delete_courier):
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создать курьера без логина или пароля')
    @pytest.mark.parametrize("payload", [
        {"password": PASSWORD, "firstName": FIRST_NAME},  # No login
        {"login": LOGIN, "firstName": FIRST_NAME}  # No password
    ])
    def test_create_courier_without_required_field_show_message_bad_request(self, payload):
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }

    @allure.title('Создать курьера c логином, который уже существует в системе')
    def test_create_courier_with_login_already_exists_show_message_conflict(self, create_courier, delete_courier):
        payload = {"login": LOGIN, "password": generate_password(), "firstName": generate_first_name()}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        assert response.status_code == 409
        assert response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }
