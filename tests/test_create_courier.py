import pytest
import allure
import requests

from helpers.helper import *
from helpers.data import *


class TestCreateCourier:

    @allure.title("Создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self, courier):
        login, password = courier
        payload = {"login": login, "password": password}

        with allure.step("Отправка запроса на создание курьера с дублирующимся логином"):
            response = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)

        with allure.step("Проверяем, что сервер вернул ошибку 409 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["conflict"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["login_already_exists"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Создать курьера и получить корректный ответ")
    def test_create_courier_success(self):
        payload = {
            "login": generate_login(),
            "password": generate_password(),
            "firstName": generate_first_name(),
        }

        with allure.step("Отправка запроса на создание нового курьера"):
            response = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)

        with allure.step("Проверяем, что сервер вернул статус 201 и успешный ответ"):
            assert response.status_code == EXPECTED_STATUS_CODES["created"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == {"ok": True}, \
                f"Unexpected response body: {response.json()}"

    @allure.title("Создать курьера без логина или пароля")
    @pytest.mark.parametrize("payload", [
        {"password": generate_password(), "firstName": generate_first_name()},  # Нет логина
        {"login": generate_login(), "firstName": generate_first_name()}  # Нет пароля
    ])
    def test_create_courier_without_required_field_show_message_bad_request(self, payload):
        with allure.step("Отправка запроса на создание курьера без обязательного поля"):
            response = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)

        with allure.step("Проверяем, что сервер вернул ошибку 400 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["bad_request"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["insufficient_data"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Создать курьера c логином, который уже существует в системе")
    def test_create_courier_with_login_already_exists_show_message_conflict(self, courier):
        login, _ = courier
        payload = {"login": login, "password": generate_password(), "firstName": generate_first_name()}

        with allure.step("Отправка запроса на создание курьера с уже существующим логином"):
            response = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)

        with allure.step("Проверяем, что сервер вернул ошибку 409 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["conflict"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["login_already_exists"], \
                f"Unexpected response body: {response.json()}"
