# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input('Please, enter a number n = ')
nn = n + n
nnn = nn + n
print(f'The sum n + nn + nnn is {n} + {nn} + {nnn} = {int(n) + int(nn) + int(nnn)}')
