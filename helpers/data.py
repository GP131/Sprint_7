import random
import datetime

from faker import Faker

faker = Faker()


def generate_first_name():
    return faker.first_name()


def generate_password():
    return faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)


def generate_login():
    return faker.user_name()


def generate_last_name():
    return faker.last_name()


def generate_address():
    return faker.street_address()


def generate_metro_station():
    return random.randint(1, 5)


def generate_phone():
    return faker.phone_number()


def generate_rent_time():
    return random.randint(1, 5)


def generate_delivery_date():
    return str(datetime.date.today())


def generate_comment():
    return faker.text(max_nb_chars=100)


def generate_color():
    return [random.choice(['BLACK', 'GREY'])]


def generate_limit_orders():
    return random.randint(2, 11)


def generate_courier_id():
    return random.randint(99999, 999999)


EXPECTED_STATUS_CODES = {
    "success": 200,
    "created": 201,
    "bad_request": 400,
    "not_found": 404,
    "conflict": 409
}

ERROR_MESSAGES = {
    "missing_data": {"code": 400, "message": "Недостаточно данных для поиска"},
    "courier_not_found": {"code": 404, "message": "Курьера с таким id не существует"},
    "courier_not_exist": {"code": 404, "message": "Курьера с таким id нет."},
    "account_not_found": {'code': 404, 'message': "Учетная запись не найдена"},
    "not_found": {"code": 404, "message": "Not Found."},
    "insufficient_data": {"code": 400, "message": "Недостаточно данных для создания учетной записи"},
    "insufficient_data_login": {"code": 400, "message": "Недостаточно данных для входа"},
    "login_already_exists": {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."},
    "courier_already_exists": {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."},
    "order_not_found": {"code": 404, "message": "Заказ не найден"},
    "order_not_exist": {"code": 404, "message": "Заказа с таким id не существует"}
}
