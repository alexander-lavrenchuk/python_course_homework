"""
Реализовать функцию int_func(), принимающую слова из маленьких
латинских букв и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
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


user_answer = input('Enter string of symbols in latin lowercase: ')
print(capitalize_first_letter(user_answer))
