# Sprint_7 QA Practicum  

API-тестирование сервиса "Яндекс.Самокат" с использованием Pytest и Allure  

## Тестовые сценарии  

1. **Авторизация курьера** – проверка входа в систему  
   - `test_order_courier.py`  

2. **Создание курьера** – проверка успешного создания курьера  
   - `test_create_courier.py`  

3. **Создание заказа** – проверка успешного создания заказа  
   - `test_create_order.py`  

4. **Получение списка заказов** – проверка, что API возвращает список заказов  
   - `test_get_list_orders.py`  

5. **Получение заказа по ID** – проверка поиска заказа по идентификатору  
   - `test_get_order_by_id.py`  

6. **Удаление курьера** – удаление существующего и несуществующего курьера  
   - `test_delete_courier.py`  

7. **Принятие заказа курьером** – проверка возможности назначения заказа курьеру  
   - `test_accept_order.py`  

8. **Обработка ошибок API** – тесты для несуществующих заказов, курьеров и некорректных запросов  
   - `test_accept_order.py`  
   - `test_delete_courier.py`  
   - `test_get_order_by_id.py`  
   - `test_order_courier.py`  
   - `test_create_courier.py`  

## Тестовый фреймворк  

* pytest / requests / allure  

### Установить зависимости:  

> pip install -r requirements.txt  

### Запустить все тесты:  

> $env:PYTHONPATH = "."  
> pytest -v  

### Запустить тесты с генерацией отчета Allure:  

> $env:PYTHONPATH = "."  
> pytest -v --alluredir=allure_results  

### Посмотреть отчет в браузере:  

> allure serve allure_results  
