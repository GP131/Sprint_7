import allure
import pytest
import requests

from helpers import generate_password, generate_login
from data import MAIN_URL, LOGIN_COURIER_URL, LOGIN, PASSWORD


class TestLoginCourier:

    @allure.title('Выполнить логин с логином и паролем')
    def test_login_courier_with_login_password_true(self, create_courier):
        payload = {"login": LOGIN, "password": PASSWORD}
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response: {response.text}"
        assert "id" in response.json() and response.json()[
            "id"], f"Courier ID is missing in response: {response.json()}"

    @allure.title('Выполнить логин с несуществующим логином и паролем')
    def test_login_courier_with_bad_login_password_return_message_error(self):
        payload = {"login": generate_login(), "password": generate_password()}
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 404, f"Unexpected status code: {response.status_code}, response: {response.text}"
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Выполнить логин без логина или пароля')
    @pytest.mark.parametrize('login_courier, password_courier', [[generate_login(), ''], ['', generate_password()]])
    def test_login_courier_without_login_or_password_return_message_error(self, login_courier, password_courier):
        payload = {"login": login_courier, "password": password_courier}
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 400, f"Unexpected status code: {response.status_code}, response: {response.text}"
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Логин возвращает идентификатор курьера')
    def test_login_courier_return_id_courier(self, create_courier):
        payload = {"login": LOGIN, "password": PASSWORD}
        response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 200, f"Unexpected status code: {response.status_code}, response: {response.text}"
        assert "id" in response.json() and response.json()[
            "id"], f"Courier ID is missing in response: {response.json()}"
