import pytest
import requests
import allure

from data import *
from helpers import *


@pytest.fixture()
def create_courier():
    payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
    response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)
    assert response.status_code in [201, 409], f"Unexpected response: {response.text}"


@pytest.fixture()
def delete_courier():
    yield

    payload = {"login": LOGIN, "password": PASSWORD}
    response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)

    if response.status_code == 200 and 'id' in response.json():
        id_courier = response.json()['id']
        requests.delete(f'{MAIN_URL}{CREATE_COURIER_URL}/{id_courier}')


import pytest
from helpers import (
    generate_first_name, generate_password, generate_address, generate_metro_station,
    generate_phone, generate_rent_time, generate_delivery_date, generate_comment, generate_color
)


@pytest.fixture
def payload_order():
    return {
        "firstName": generate_first_name(),
        "lastName": generate_password(),
        "address": generate_address(),
        "metroStation": generate_metro_station(),
        "phone": generate_phone(),
        "rentTime": generate_rent_time(),
        "deliveryDate": generate_delivery_date(),
        "comment": generate_comment(),
        "color": generate_color()
    }
