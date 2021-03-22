"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове.
"""
user_input = input('Input string: ')
user_input_list = user_input.split()
row_num = 0
for el in user_input_list:
    row_num += 1
    print(f'{row_num} row: {el[:10]}')
