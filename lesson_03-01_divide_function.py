"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

def division(numerator, denominator):
    """
    Divides numerator by denominator and returns the result
    :param numerator: the value to be divided
    :param denominator: the value to divide by
    :return: the result of division of the first argument by the second argument
    """
    if not denominator:
        print(f"Can't divide by zero")
        return
    return numerator / denominator


value_for_numerator = float(input('Enter numerator: '))
value_for_denominator = float(input('Enter denominator: '))
result = division(value_for_numerator, value_for_denominator)
if result:
    print(f'{value_for_numerator} divided by {value_for_denominator} is {result}')
