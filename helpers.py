import datetime
import random

from faker import Faker


def generate_first_name():
    return Faker().first_name()


def generate_password():
    return Faker().password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)


def generate_login():
    return Faker().user_name()


def generate_last_name():
    return Faker().last_name()


def generate_address():
    return Faker().street_address()


def generate_metro_station():
    return random.randint(1, 5)


def generate_phone():
    return Faker().phone_number()


def generate_rent_time():
    return random.randint(1, 5)


def generate_delivery_date():
    return str(datetime.date.today())


def generate_comment():
    return Faker().text(max_nb_chars=100)


def generate_color():
    list_color = []
    random_color = random.choice(['BLACK', 'GREY'])
    list_color.append(random_color)
    return list_color


def generate_limit_orders():
    return random.randint(2, 11)


def generate_courier_id():
    return random.randint(99999, 999999)
