# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('Please, enter a number: '))
number = user_number
max_digit = number % 10
while number // 10 > 0 and max_digit < 9:
    number = number // 10
    max_digit = max(max_digit, number % 10)
print(f'Maximum digit in number {user_number} is {max_digit}')
