import pytest
import allure

from helpers.helper import *
from helpers.data import *


@pytest.fixture()
def courier():
    login = generate_login()
    password = generate_password()
    first_name = generate_first_name()

    with allure.step("Создание нового курьера"):
        create_courier(login, password, first_name)
    yield login, password
    with allure.step("Удаление созданного курьера"):
        delete_courier(login, password)


@pytest.fixture()
def new_order():
    with allure.step("Создание нового заказа"):
        order_data = ORDER_PAYLOAD.copy()
        track = create_order()
        order_data["track"] = track

    yield order_data

    with allure.step("Удаление созданного заказа"):
        delete_order(track)
