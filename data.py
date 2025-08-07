from helpers import *


class UserData:
    email = 'kostya_kuznecov_22_991@yandex.ru'
    password = '123456'
    username = 'Костя'

    data_with_empty_field = [
        {'email': '',
         'password': create_random_password(),
         'name': create_random_username()},
        {'email': create_random_email(),
         'password': '',
         'name': create_random_username()},
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''}]


class IngredientData:
    burger_1 = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa6f']

    burger_2 = ['61c0c5a71d1f82001bdaaa6c', '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa70']

    invalid_hash_ingredient = ['6105cc171d1f90000brasic6']


class Responses:
    UNAUTHORIZED = {
        "success": False,
        "message": "You should be authorised"
    }

    NO_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    USER_EXIST = {
        'success': False,
        'message': 'User already exists'
    }

    REQUIRED_FIELDS = {
        'success': False,
        'message': 'Email, password and name are required fields'
    }

    INCORRECT_DATA = {
        "success": False,
        "message": "email or password are incorrect"
    }
