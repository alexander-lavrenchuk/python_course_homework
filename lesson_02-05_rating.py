"""
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
print(f'Rating structure is {my_list}')
user_answer = ''
while not user_answer == 'q':
    if user_answer.isdigit():
        new_entry = int(user_answer)
        i = -1
        while not abs(i) > len(my_list):
            if my_list[i] >= new_entry:
                break
            i -= 1
        if i == -1:
            my_list.append(new_entry)
        else:
            i = (i + 1, 0)[abs(i) > len(my_list)]
            my_list.insert(i, new_entry)
        print(f'Rating structure is {my_list}')
    user_answer = input("Enter new rating entry or character 'q' to quit the program: ")
