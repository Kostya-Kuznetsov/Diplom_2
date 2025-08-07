import pytest
import allure
import requests
from urls import *
from data import *


@pytest.fixture
@allure.title('Фикстура для создания пользователя и удаления после теста')
def create_and_delete_new_user():
    payload = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()}
    response = requests.post(URLS.USER_REGISTER, data=payload)
    response_body = response.json()

    yield payload, response_body

    access_token = response_body['accessToken']
    requests.delete(URLS.USER_DELETE, headers={'Authorization': access_token})


@pytest.fixture
@allure.title('Фикстура создания пользователя и заказа пользователя')
def create_user_and_order_with_delete_user(create_and_delete_new_user):
    access_token = create_and_delete_new_user[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [IngredientData.burger_2]}
    response_body = requests.post(URLS.ORDER_CREATE, data=payload, headers=headers)

    yield access_token, response_body

    requests.delete(URLS.USER_DELETE, headers={'Authorization': access_token})
