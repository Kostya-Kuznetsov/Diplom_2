import pytest
import allure
from data import *
from urls import *
import requests


class TestRegistration:
    @allure.title('Создание уникального пользователя')
    @allure.description('Создается аккаунт с рандомными данными и удаляется после теста.'
                       'Проверка кода, тела ответа, получение accessToken и refreshToken.')
    def test_registration_uniq_user(self, create_and_delete_new_user):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(URLS.USER_REGISTER, data=payload)
        answer = response.json()
        assert response.status_code == 200
        assert answer['success'] is True
        assert 'accessToken' in answer.keys()
        assert 'refreshToken' in answer.keys()
        assert answer['user']['email'] == payload['email']
        assert answer['user']['name'] == payload['name']


    @allure.title('Создание пользователя, который уже зарегистрирован')
    @allure.description('Используем email зарегистрированного пользователя')
    def test_registration_not_uniq_user(self):
        payload = {
            'email': UserData.email,
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(URLS.USER_REGISTER, data=payload)
        assert response.status_code == 403
        assert response.json() == Responses.USER_EXIST


    @allure.title('Создание пользователя с незаполненным полем')
    @allure.description('При помощи параметризации производим три теста, в каждом из которых не заполнено одно из полей')
    @pytest.mark.parametrize('credentials', UserData.data_with_empty_field)
    def test_registration_with_empty_field(self, credentials):
        response = requests.post(URLS.USER_REGISTER, data=credentials)
        assert response.status_code == 403
        assert response.json() == Responses.REQUIRED_FIELDS
