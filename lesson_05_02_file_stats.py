"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""
data_file_name = 'data_2.log'
try:
    with open(data_file_name) as file_obj:
        line_num = 0
        words_in_line = []
        for line in file_obj:
            line_num += 1
            words_in_line = line.split()
            words_num = len(words_in_line)
            suffix = 'words.' if words_num > 1 else 'word.'
            msg_1 = f'Line {line_num} contains '
            msg_2 = f'{words_num} {suffix}' if words_num > 0 else 'no words.'
            print(msg_1 + msg_2)
        if line_num == 0:
            print('File is empty!')
except IOError:
    print('I/O Error!')
