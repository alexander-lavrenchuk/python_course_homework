"""
6. Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
повторение элементов списка прекратится.
"""
from itertools import count
from itertools import cycle
# First task
first_el = int(input('Enter integer number for start element of count: '))
last_el = int(input('Enter integer number for last element of count: '))
for el in count(first_el):
    if el > last_el:
        break
    print(el)

# Second task
cycle_list = list(input('Enter list of elements divided by spaces: ').split())
steps_num = int(input('Enter integer number for steps of list elements cycle: '))
current_step = 0
for el in cycle(cycle_list):
    current_step += 1
    if current_step > steps_num:
        break
    print(f'Step: {current_step}, list element: {el}')
