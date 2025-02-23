import allure
import requests

from data import *


class TestListOrders:

    @allure.title('Получить заказы и проверить, что тело ответа возвращает список заказов')
    def test_get_orders_return_list_orders(self):
        params = {"limit": LIMIT_ORDERS}
        response = requests.get(f'{MAIN_URL}{GET_LIST_ORDERS_URL}', params=params)

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response: {response.text}"

        response_json = response.json()
        assert "orders" in response_json, f"Response does not contain 'orders': {response_json}"

        assert isinstance(response_json["orders"], list), f"'orders' is not a list: {response_json['orders']}"
        assert len(response_json["orders"]) > 0, "Order list is empty, but expected non-empty list."
