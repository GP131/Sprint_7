import requests

from helpers.urls import *
from helpers.data import *

ORDER_PAYLOAD = {
    "firstName": generate_first_name(),
    "lastName": generate_last_name(),
    "address": generate_address(),
    "metroStation": generate_metro_station(),
    "phone": generate_phone(),
    "rentTime": generate_rent_time(),
    "deliveryDate": generate_delivery_date(),
    "comment": generate_comment(),
    "color": generate_color()
}


def create_order():
    response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=ORDER_PAYLOAD)

    if response.status_code == 201:
        return response.json().get("track")
    else:
        raise Exception(f"Order creation failed: {response.status_code}, response: {response.text}")


def delete_order(track):
    response = requests.put(f"{MAIN_URL}{CANCEL_ORDER_URL}", params={"track": track})

    if response.status_code != 200:
        raise Exception(f"Failed to delete order {track}: {response.status_code}, response: {response.text}")


def create_courier(login, password, first_name):
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(f"{MAIN_URL}{CREATE_COURIER_URL}", json=payload)

    if response.status_code == 201:
        return login  # Use login to fetch ID later
    elif response.status_code == 409:
        print("Courier already exists.")
        return None
    else:
        raise Exception(f"Failed to create courier: {response.status_code}, response: {response.text}")


def delete_courier(login, password):
    login_payload = {"login": login, "password": password}
    response = requests.post(f"{MAIN_URL}{LOGIN_COURIER_URL}", json=login_payload)

    if response.status_code == 200 and "id" in response.json():
        courier_id = response.json()["id"]
        requests.delete(f"{MAIN_URL}{CREATE_COURIER_URL}/{courier_id}")
    else:
        print(f"Failed to log in and delete courier: {response.status_code}, response: {response.text}")
