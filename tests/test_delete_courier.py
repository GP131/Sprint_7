import allure
import requests
import random

from data import *


class TestDeleteCourier:

    @allure.title('Удалить курьера с несуществующим id')
    def test_delete_courier_not_exist_id_return_message_error(self):
        non_existent_id = random.randint(100000, 999999)
        response = requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}/{non_existent_id}')

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}

    @allure.title('Удалить курьера')
    def test_delete_courier_return_ok_true(self, create_courier):
        payload = {"login": LOGIN, "password": PASSWORD}
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)
        assert response.status_code == 200

        id_courier = response.json().get('id')
        assert id_courier, "Courier ID was not returned from the login request"

        response = requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}/{id_courier}')

        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure.title('Удалить курьера без id курьера')
    def test_delete_courier_without_id_return_message_not_found(self):
        response = requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}')

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Not Found.'}
