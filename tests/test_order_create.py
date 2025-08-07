import allure
import pytest
from data import *
from urls import *
import requests


class TestOrderCreate:
    @allure.title('Создание заказа с ингредиентами авторизованным пользователем')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_order_create_authorized(self, create_and_delete_new_user, burger_ingredients):
        headers = {'Authorization': create_and_delete_new_user[1]['accessToken']}
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(URLS.ORDER_CREATE, data=payload, headers=headers)
        answer = response.json()
        assert response.status_code == 200
        assert answer['success'] is True
        assert 'name' in answer.keys()
        assert 'number' in answer['order'].keys()

    @allure.title('Создание заказа с ингредиентами без авторизации')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_order_create_not_authorized(self, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(URLS.ORDER_CREATE, data=payload, headers=URLS.headers)
        assert response.status_code == 401
        assert response.json() == Responses.UNAUTHORIZED

    @allure.title('Создание заказа без ингредиентов авторизованным пользователем')
    def test_order_create_no_ingredients_authorized(self, create_and_delete_new_user):
        headers = {'Authorization': create_and_delete_new_user[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(URLS.ORDER_CREATE, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json() == Responses.NO_INGREDIENTS

    @allure.title('Создание заказа без ингредиентов, без авторизации')
    def test_order_ceate_no_ingredients_not_authorized(self):
        payload = {'ingredients': []}
        response = requests.post(URLS.ORDER_CREATE, data=payload, headers=URLS.headers)
        assert response.status_code == 400
        assert response.json() == Responses.NO_INGREDIENTS

    @allure.title('Создание заказа с невалидным хэшем нигредиента')
    def test_order_create_invalid_hash_authorized(self, create_and_delete_new_user):
        headers = {'Authorization': create_and_delete_new_user[1]['accessToken']}
        payload = {'ingredients': [IngredientData.invalid_hash_ingredient]}
        response = requests.post(URLS.ORDER_CREATE, data=payload, headers=headers)
        assert response.status_code == 500
