"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce
from decimal import Decimal
evens_list = [el for el in range(100, 1001) if el % 2 == 0]
result = Decimal(reduce(lambda m, x: m * x, evens_list))
print(f'The list of even numbers in range [100, 1000] including both boundaries is {evens_list}')
print(f'The total multiply of evens list elements is {result:.4e}')
