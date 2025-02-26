import allure
import requests

from helpers.helper import *
from helpers.data import *


class TestGetOrderById:

    @allure.title("Получить заказ по его id")
    def test_get_order_by_id_true(self):
        with allure.step("Создание тестового заказа"):
            track = create_order()
            assert track, "Order ID (track) was not returned after order creation"

        with allure.step(f"Получение заказа по ID {track}"):
            params = {"t": track}
            response = requests.get(f"{MAIN_URL}{GET_ORDER_BY_ID_URL}", params=params)

        with allure.step("Проверяем, что статус-код 200 и заказ найден"):
            assert response.status_code == EXPECTED_STATUS_CODES["success"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert "order" in response.json(), f"Response does not contain 'order': {response.json()}"

        with allure.step("Удаление тестового заказа после проверки"):
            delete_order(track)

    @allure.title("Получить заказ без его id")
    def test_get_order_without_id_return_bad_request(self):
        with allure.step("Отправка запроса без ID заказа"):
            params = {"t": ""}
            response = requests.get(f"{MAIN_URL}{GET_ORDER_BY_ID_URL}", params=params)

        with allure.step("Проверяем, что статус-код 400 и вернулось сообщение об ошибке"):
            assert response.status_code == EXPECTED_STATUS_CODES["bad_request"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["missing_data"], \
                f"Unexpected response body: {response.json()}"

    @allure.title("Получить заказ по несуществующему id")
    def test_get_order_by_not_exist_id_return_not_found(self):
        non_existing_id = 999999999

        with allure.step(f"Отправка запроса на получение заказа по несуществующему ID {non_existing_id}"):
            params = {"t": non_existing_id}
            response = requests.get(f"{MAIN_URL}{GET_ORDER_BY_ID_URL}", params=params)

        with allure.step("Проверяем, что статус-код 404 и вернулось сообщение об ошибке"):
            assert response.status_code == EXPECTED_STATUS_CODES["not_found"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert response.json() == ERROR_MESSAGES["order_not_found"], \
                f"Unexpected response body: {response.json()}"
