"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
from random import randint
from functools import reduce
data_file_name = 'data_5.log'
inf = -100
sup = 100
total_num = int(1e4)
total_sum = 0
num_list = [randint(inf, sup) for i in range(total_num)]
with open(data_file_name, 'w') as data_file:
    for n in num_list:
        print(n, end=' ', file=data_file)
with open(data_file_name) as data_file:
    total_sum = reduce(lambda x, y: x + y, [float(w) for w in data_file.read().split()])
print(f'The total sum of numbers in {data_file_name} file is {total_sum}.')
