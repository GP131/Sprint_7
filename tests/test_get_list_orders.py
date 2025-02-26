import allure
import requests

from helpers.urls import *
from helpers.data import *
from helpers.helper import *


class TestListOrders:

    @allure.title("Получить заказы и проверить, что тело ответа возвращает список заказов")
    def test_get_orders_return_list_orders(self):
        with allure.step("Создание тестового заказа, чтобы список заказов не был пустым"):
            track = create_order()

        limit_orders = generate_limit_orders()

        with allure.step(f"Отправка запроса на получение списка заказов с лимитом {limit_orders}"):
            response = requests.get(f"{MAIN_URL}{GET_LIST_ORDERS_URL}", params={"limit": limit_orders})

        with allure.step("Проверяем, что статус-код ответа 200"):
            assert response.status_code == EXPECTED_STATUS_CODES["success"], \
                f"Unexpected status code: {response.status_code}, response: {response.text}"

        response_json = response.json()

        with allure.step("Проверяем, что ответ содержит ключ 'orders'"):
            assert "orders" in response_json, \
                f"Response does not contain 'orders': {response_json}"

        with allure.step("Проверяем, что 'orders' является списком и не пустой"):
            assert isinstance(response_json["orders"], list), \
                f"'orders' is not a list: {response_json['orders']}"
            assert len(response_json["orders"]) > 0, "Order list is empty, but expected non-empty list."

        with allure.step("Удаление тестового заказа после проверки"):
            delete_order(track)
