import allure
import requests

from data import MAIN_URL, CREATE_ORDER_URL, GET_ORDER_BY_ID_URL


class TestGetOrderById:

    @allure.title('Получить заказ по его id')
    def test_get_order_by_id_true(self, payload_order):
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)
        assert response.status_code == 201, f"Failed to create order: {response.status_code}, response: {response.text}"

        order_id = response.json().get('track')
        assert order_id, f"Order ID not found in response: {response.json()}"

        params = {"t": order_id}
        response = requests.get(f'{MAIN_URL}{GET_ORDER_BY_ID_URL}', params=params)

        assert response.status_code == 200, f"Failed to get order: {response.status_code}, response: {response.text}"
        assert "order" in response.json(), f"Response does not contain 'order': {response.json()}"

    @allure.title('Получить заказ без его id')
    def test_get_order_without_id_return_bad_request(self):
        params = {"t": ""}
        response = requests.get(f'{MAIN_URL}{GET_ORDER_BY_ID_URL}', params=params)

        assert response.status_code == 400, f"Unexpected status code: {response.status_code}, response: {response.text}"
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title('Получить заказ по несуществующему id')
    def test_get_order_by_not_exist_id_return_not_found(self):
        non_existing_id = 999999999
        params = {"t": non_existing_id}
        response = requests.get(f'{MAIN_URL}{GET_ORDER_BY_ID_URL}', params=params)

        assert response.status_code == 404, f"Unexpected status code: {response.status_code}, response: {response.text}"
        assert response.json() == {'code': 404, 'message': 'Заказ не найден'}
