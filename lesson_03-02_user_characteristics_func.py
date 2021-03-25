"""
Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


def user_characteristics(name, last_name, year_of_birth, residential_city, email, phone):
    """
    Displays user characteristics
    :param name: user name
    :param last_name: user last name
    :param year_of_birth: user year of birth
    :param residential_city: user city of residential
    :param email: user email
    :param phone: user phone
    :return: None
    """
    print(f'User characteristics>>> name: {name}, last_name: {last_name}, '
          f'year of birth: {year_of_birth}, city of residential: {residential_city}, '
          f'email: {email}, phone: {phone}.')


user_characteristics(last_name='Lavrenchuk', name='Alexander',
                     year_of_birth=1982, residential_city='Moscow',
                     phone='+7(905)758-5775', email='lavrenchuk@yandex.ru')
