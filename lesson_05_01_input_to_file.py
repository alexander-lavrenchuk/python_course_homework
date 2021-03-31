"""
1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""
output_file_name = 'data_1.log'
print('Enter string for log or empty string to end the program.')
string_num = 0
strings = []
while True:
    string_num += 1
    user_input = input(f'String {string_num}: ')
    if not user_input:
        break
    strings.append(user_input + '\n')
try:
    with open(output_file_name, 'w') as file_obj:
        file_obj.writelines(strings)
except IOError:
    print('I/O Error!')
print(f'Check file {output_file_name} for saved inputs.')
