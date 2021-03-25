"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def is_number(s_number):
    """
    Check whether it is possible to convert string argument to float
    :param s_number: string argument
    :return: True if it is possible to convert argument to float, or false otherwise
    """
    try:
        float(s_number)
        return True
    except ValueError:
        return False


def row_sum(l_total_sum, s_brake_command, l_is_brake_command_entered, t_row):
    """
    Calculates total sum of row
    :param l_total_sum: The list of one element representing the total sum
    :param s_brake_command: The string defining brake command
    :param l_is_brake_command_entered: The list of one element representing whether brake command was entered
    :param t_row: The tuple of user input elements separated by spaces
    :return: None, but changes one element lists with total sum and flag of encountered brake command
    """
    for el in t_row:
        if is_number(el):
            l_total_sum[0] += float(el)
        else:
            l_is_brake_command_entered[0] = True if el == s_brake_command else l_is_brake_command_entered[0]
            break


total_sum = [0]
brake_command = 'q'
is_brake_command_entered = [False]
while not is_brake_command_entered[0]:
    row = input(f"Enter a row of numbers to sum up. Specify '{brake_command}' to stop the program. \n: ").split()
    row_sum(total_sum, brake_command, is_brake_command_entered, row)
    print(f"The total sum of entered numbers before brake command '{brake_command}' is {total_sum[0]}.")
print('Encountered brake command. Program has been ended.')
