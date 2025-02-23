import pytest
import allure
import requests

from data import MAIN_URL, CREATE_ORDER_URL


class TestCreateOrder:

    @allure.title('Создать заказ самоката с разными цветами')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_various_colors(self, payload_order, color):
        payload_order["color"] = color
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создать заказ и получить номер заказа')
    def test_create_order_returns_track_number(self, payload_order):
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        assert response.status_code == 201
        assert 'track' in response.json()
