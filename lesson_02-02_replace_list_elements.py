"""
2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
"""
user_input = input('Input list of elements, separated by string "\\\\\\" (triple backslash sign) : ')
list_obj = user_input.split('\\\\\\')
i = 0
list_obj_count = len(list_obj)
while not i > 2 * (list_obj_count // 2 - 1):
    list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
    i += 2
print(f'Modified list is:\n{list_obj}')
