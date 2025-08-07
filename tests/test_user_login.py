import allure
from data import *
from urls import *
import requests


class TestLogin:
    @allure.title('Проверка логина под существующим пользователем')
    def test_registration_uniq_user(self, create_and_delete_new_user):
        payload = create_and_delete_new_user[0]
        response = requests.post(URLS.USER_AUTH, data=payload)
        answer = response.json()
        assert response.status_code == 200
        assert answer['success'] is True
        assert 'accessToken' in answer.keys()
        assert 'refreshToken' in answer.keys()
        assert answer['user']['email'] == payload['email']
        assert answer['user']['name'] == payload['name']

    @allure.title('Проверка аутентификации с неверным логином')
    def test_login_with_wrong_login(self):
        payload = {
            'email': create_random_email(),
            'password': UserData.password,
        }
        response = requests.post(URLS.USER_AUTH, data=payload)
        assert response.status_code == 401
        assert response.json() == Responses.INCORRECT_DATA

    @allure.title('Проверка аутентификации с неверным паролем')
    def test_login_with_wrong_password(self):
        payload = {
            'email': UserData.email,
            'password': create_random_password(),
        }
        response = requests.post(URLS.USER_AUTH, data=payload)
        assert response.status_code == 401
        assert response.json() == Responses.INCORRECT_DATA
