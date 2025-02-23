from helpers import *

MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
CREATE_COURIER_URL = '/api/v1/courier'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
GET_LIST_ORDERS_URL = '/api/v1/orders'
ACCEPT_ORDER_URL = '/api/v1/orders/accept'
GET_ORDER_BY_ID_URL = '/api/v1/orders/track'

LOGIN = generate_login()
PASSWORD = generate_password()
FIRST_NAME = generate_first_name()
LIMIT_ORDERS = generate_limit_orders()
COURIER_ID = generate_courier_id()
