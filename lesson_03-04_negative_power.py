"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func1(f_x, i_y):
    """
    Powers a real positive number x to an integer negative exponent y using operator **
    :param f_x: base
    :param i_y: exponent
    :return: float number equals to a base powered by an exponent
    """
    return f_x ** i_y


def my_func2(f_x, i_y):
    """
    Powers a real positive number x to an integer negative exponent y using circle for in
    :param f_x: base
    :param i_y: exponent
    :return: float number equals to a base powered by an exponent
    """
    result = 1.0
    for el in range(abs(i_y)):
        result /= f_x
    return result


def check_for_correct_input(s_input):
    """
    Checks for correct input. Input must be a string of two words.
    First of them must be a positive real number.
    And the second must be a negative integer number
    :param s_input: string to check
    :return: True if input is correct, or false otherwise.
    """
    t_input = s_input.split()
    if len(t_input) == 2:
        s_x, s_y = t_input
        try:
            f_x = float(s_x)
            try:
                i_y = int(s_y)
                if f_x <= 0:
                    print('First argument x must be a positive real number.')
                elif i_y >= 0:
                    print('Second argument y must be a negative integer number.')
                else:
                    return True
            except ValueError:
                print('Second argument y must be a negative integer number.')
                return False
        except ValueError:
            print('First argument x must be a positive real number.')
            return False
    else:
        return False


user_answer = input('Enter two numbers a real positive x and an integer negative y divided by space: ')

if check_for_correct_input(user_answer):
    t_user_answer = user_answer.split()
    fx = float(t_user_answer[0])
    iy = int(t_user_answer[1])
    answer = my_func1(fx, iy)
    print(f'The result x^y using operator ** is {answer}.')
    answer = my_func2(fx, iy)
    print(f'The result x^y using circle for in is {answer}.')
else:
    print('Wrong input.')
