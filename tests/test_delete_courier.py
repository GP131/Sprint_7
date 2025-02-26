import allure
import random
import requests

from helpers.urls import *
from helpers.data import EXPECTED_STATUS_CODES, ERROR_MESSAGES
from helpers.helper import *


class TestDeleteCourier:

    @allure.title("Удалить курьера с несуществующим id")
    def test_delete_courier_not_exist_id_return_message_error(self):
        non_existent_id = random.randint(100000, 999999)

        with allure.step("Отправка запроса на удаление несуществующего курьера"):
            response = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{non_existent_id}")

        with allure.step("Проверяем, что сервер вернул ошибку 404 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["not_found"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["courier_not_exist"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Удалить курьера")
    def test_delete_courier_return_ok_true(self, courier):
        login, password = courier

        with allure.step("Логин курьера для получения его ID"):
            response_courier = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}",
                                             json={"login": login, "password": password})
            assert response_courier.status_code == EXPECTED_STATUS_CODES["success"], \
                f"Unexpected status code: {response_courier.status_code}, response: {response_courier.text}"

            courier_id = response_courier.json().get("id")
            assert courier_id, "Courier ID was not returned from the login request"

        with allure.step("Отправка запроса на удаление курьера"):
            response = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_id}")

        with allure.step("Проверяем, что сервер вернул 200 и {'ok': True}"):
            assert response.status_code == EXPECTED_STATUS_CODES["success"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == {"ok": True}, f"Unexpected response body: {response.json()}"

    @allure.title("Удалить курьера без id курьера")
    def test_delete_courier_without_id_return_message_not_found(self):
        with allure.step("Отправка запроса на удаление без ID курьера"):
            response = requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}")

        with allure.step("Проверяем, что сервер вернул ошибку 404 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["not_found"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["not_found"], \
                f"Unexpected response body: {response.json()}"
