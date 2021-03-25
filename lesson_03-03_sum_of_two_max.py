"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    """
    Determines the two maximal arguments of three given and returns its sum
    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    """
    try:
        f_arg1 = float(arg1)
        f_arg2 = float(arg2)
        f_arg3 = float(arg3)
    except ValueError:
        print('Arguments must be numbers.')
        return None
    else:
        arg_list = [f_arg1, f_arg2, f_arg3]
        var_list = arg_list.copy()
        max_list = []
        for el in range(2):
            max_var = max(var_list)
            var_list.remove(max_var)
            max_list.append(max_var)
        return sum(arg_list)-min(arg_list)
        # or for only three arguments one can use formula sum(arg_list) - min(arg_list)
        # return sum(max_list)


user_input = input('Enter three numbers, delimited by space: ')
x, y, z = user_input.split()
sum_of_two_max = my_func(x, y, z)
if sum_of_two_max:
    print(f'The sum of the two maximal number of three entered is {sum_of_two_max}.')
