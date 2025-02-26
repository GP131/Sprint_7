import pytest
import allure
import requests

from helpers.helper import MAIN_URL
from helpers.data import EXPECTED_STATUS_CODES
from helpers.urls import CREATE_ORDER_URL


class TestCreateOrder:

    @allure.title("Создать заказ самоката с разными цветами")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_various_colors(self, new_order, color):
        new_order["color"] = color

        with allure.step("Отправка запроса на создание заказа"):
            response = requests.post(f"{MAIN_URL}{CREATE_ORDER_URL}", json=new_order)

        with allure.step("Проверяем, что заказ успешно создан и есть номер заказа"):
            assert response.status_code == EXPECTED_STATUS_CODES["created"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert "track" in response.json(), "Response does not contain 'track' field"

    @allure.title("Создать заказ и получить номер заказа")
    def test_create_order_returns_track_number(self, new_order):
        with allure.step("Отправка запроса на создание заказа"):
            response = requests.post(f"{MAIN_URL}{CREATE_ORDER_URL}", json=new_order)

        with allure.step("Проверяем, что заказ успешно создан и есть номер заказа"):
            assert response.status_code == EXPECTED_STATUS_CODES["created"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"
            assert "track" in response.json(), "Response does not contain 'track' field"
