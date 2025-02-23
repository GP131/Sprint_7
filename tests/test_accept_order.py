import allure
import requests
from data import *


class TestAcceptOrder:

    @allure.title('Принять заказ без id курьера')
    def test_accept_order_without_courier_id_return_message_conflict(self, create_courier, delete_courier,
                                                                     payload_order):
        response_order = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)
        order_id = response_order.json()['track']

        response = requests.put(f'{MAIN_URL}{ACCEPT_ORDER_URL}/{order_id}', params={'courierId': ""})

        assert response.status_code == 400 and response.json() == {
            'code': 400, 'message': 'Недостаточно данных для поиска'
        }

    @allure.title('Принять заказ с некорректным id курьера')
    def test_accept_order_with_incorrect_courier_id_return_message_not_found(self, payload_order):
        response_order = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)
        order_id = response_order.json()['track']

        response = requests.put(f'{MAIN_URL}{ACCEPT_ORDER_URL}/{order_id}', params={'courierId': generate_courier_id()})

        assert response.status_code == 404 and response.json() == {
            'code': 404, 'message': 'Курьера с таким id не существует'
        }

    @allure.title('Принять заказ с некорректным id заказа')
    def test_accept_order_with_incorrect_order_id_return_message_error(self, create_courier, delete_courier):
        response_courier = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data={"login": LOGIN, "password": PASSWORD})
        id_courier = response_courier.json()['id']

        response = requests.put(f'{MAIN_URL}{ACCEPT_ORDER_URL}/999999999', params={'courierId': id_courier})

        assert response.status_code == 404 and response.json() == {
            'code': 404, 'message': 'Заказа с таким id не существует'
        }
