import allure
import pytest
import requests

from helpers.helper import *
from helpers.data import *
from helpers.urls import *


class TestLoginCourier:

    @allure.title("Выполнить логин с логином и паролем")
    def test_login_courier_with_login_password_true(self):
        with allure.step("Генерация данных для курьера"):
            login = generate_login()
            password = generate_password()
            first_name = generate_first_name()

        with allure.step("Создание курьера"):
            create_courier(login, password, first_name)

        with allure.step("Логин под созданным курьером и получение ID"):
            payload = {"login": login, "password": password}
            response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload)
            assert response.status_code == EXPECTED_STATUS_CODES["success"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            courier_id = response.json().get("id")
            assert courier_id, "Courier ID not returned."

        with allure.step("Удаление тестового курьера"):
            requests.delete(f"{MAIN_URL}{DELETE_COURIER_URL}{courier_id}")

    @allure.title("Выполнить логин с несуществующим логином и паролем")
    def test_login_courier_with_bad_login_password_return_message_error(self):
        with allure.step("Отправка запроса с некорректными логином и паролем"):
            payload = {"login": generate_login(), "password": generate_password()}
            response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload)

        with allure.step("Проверяем, что статус-код 404 и сообщение об ошибке"):
            assert response.status_code == EXPECTED_STATUS_CODES["not_found"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["account_not_found"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Выполнить логин без логина или пароля")
    @pytest.mark.parametrize("login_courier, password_courier", [
        (generate_login(), ""),
        ("", generate_password())
    ])
    def test_login_courier_without_login_or_password_return_message_error(self, login_courier, password_courier):
        with allure.step(f"Отправка запроса с login={login_courier}, password={password_courier}"):
            payload = {"login": login_courier, "password": password_courier}
            response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload)

        with allure.step("Проверяем, что статус-код 400 и вернулось сообщение об ошибке"):
            assert response.status_code == EXPECTED_STATUS_CODES["bad_request"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["insufficient_data_login"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Логин возвращает идентификатор курьера")
    def test_login_courier_return_id_courier(self):
        with allure.step("Генерация данных для курьера"):
            login = generate_login()
            password = generate_password()
            first_name = generate_first_name()

        with allure.step("Создание курьера"):
            create_courier(login, password, first_name)

        with allure.step("Логин под созданным курьером и получение ID"):
            payload = {"login": login, "password": password}
            response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=payload)
            assert response.status_code == EXPECTED_STATUS_CODES["success"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            courier_id = response.json().get("id")
            assert courier_id, "Courier ID not returned."

        with allure.step("Удаление тестового курьера"):
            requests.delete(f"{MAIN_URL}{DELETE_COURIER_URL}{courier_id}")
