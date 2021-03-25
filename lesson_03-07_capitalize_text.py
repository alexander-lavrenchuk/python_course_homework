"""
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""


def capitalize_first_letter(s_word):
    """
    Capitalizes the first letter of given argument
    :param s_word: string
    :return: string
    """
    l_word = list(s_word)
    l_word[0] = str(l_word[0]).capitalize()
    return ''.join(l_word)


user_answer = input('Enter any text: ')
t_user_answer = user_answer.split()
capitalized_text = []
for el in t_user_answer:
    capitalized_text.append(capitalize_first_letter(el))
print(' '.join(capitalized_text))
