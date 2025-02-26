import allure
import requests

from helpers.helper import generate_courier_id
from helpers.urls import MAIN_URL, ACCEPT_ORDER_URL, LOGIN_COURIER_URL
from helpers.data import EXPECTED_STATUS_CODES, ERROR_MESSAGES


class TestAcceptOrder:

    @allure.title("Принять заказ без id курьера")
    def test_accept_order_without_courier_id_return_message_conflict(self, new_order):
        order_id = new_order["track"]

        with allure.step("Отправка запроса на принятие заказа без ID курьера"):
            response = requests.put(f"{MAIN_URL}{ACCEPT_ORDER_URL}/{order_id}", params={"courierId": ""})

        with allure.step("Проверяем, что сервер вернул ошибку 400 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["bad_request"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["missing_data"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Принять заказ с некорректным id курьера")
    def test_accept_order_with_incorrect_courier_id_return_message_not_found(self, new_order):
        order_id = new_order["track"]

        with allure.step("Отправка запроса на принятие заказа с неверным ID курьера"):
            response = requests.put(f"{MAIN_URL}{ACCEPT_ORDER_URL}/{order_id}",
                                    params={"courierId": generate_courier_id()})

        with allure.step("Проверяем, что сервер вернул ошибку 404 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["not_found"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["courier_not_found"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Принять заказ с некорректным id заказа")
    def test_accept_order_with_incorrect_order_id_return_message_error(self, courier):
        login, password = courier

        with allure.step("Логин курьера для получения его ID"):
            response_courier = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}",
                                             json={"login": login, "password": password})
            assert response_courier.status_code == EXPECTED_STATUS_CODES["success"], \
                f"Unexpected status code: {response_courier.status_code}, response: {response_courier.text}"
            id_courier = response_courier.json()["id"]

        with allure.step("Отправка запроса на принятие несуществующего заказа"):
            response = requests.put(f"{MAIN_URL}{ACCEPT_ORDER_URL}/999999999", params={"courierId": id_courier})

        with allure.step("Проверяем, что сервер вернул ошибку 404 и сообщение"):
            assert response.status_code == EXPECTED_STATUS_CODES["not_found"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["order_not_exist"], \
                f"Unexpected response body: {response.json()}"
