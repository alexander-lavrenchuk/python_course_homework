# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

import math
growth = 0.1
initial_distance = float(input('Enter forced distance: '))
forced_distance = initial_distance
goal_distance = float(input('Enter goal distance: '))
day_number = 1
while forced_distance < goal_distance:
    forced_distance = forced_distance * (1 + growth)
    day_number += 1
print(f'The sportsmen forced goal distance at {day_number}-th day.')
print(f'Check using formula 1 + int(ln(b) / ln(1 + i)) is '
      f'{1 + int(math.log(forced_distance / initial_distance) / math.log(1 + growth)) == day_number}')
