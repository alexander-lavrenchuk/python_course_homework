from math_round import *


def format_num(num, int_digs=0, float_digs=2, thousand_delimiter=' ', integer_delimiter=','):
    is_negative = True if num < 0 else False
    num = abs(num)
    if int_digs and len(str(int(abs(num)))) > int_digs:
        num_str = f'{num:.{float_digs}e}'
    else:
        num_str = str(math_round(num, float_digs))
    num_parts = list(num_str.split('.'))
    if num_parts[1] == '0':
        num_parts[1] = ''
        for i in range(float_digs):
            num_parts[1] += '0'
    int_parts = []
    int_part = ''
    cnt = 0
    for i in range(-1, -len(num_parts[0]) - 1, -1):
        cnt += 1
        int_part = num_parts[0][i] + int_part
        if cnt % 3 == 0:
            int_parts.insert(0, int_part)
            int_part = ''
    if int_part:
        int_parts.insert(0, int_part)
    num_parts[0] = int_parts
    res = integer_delimiter.join([thousand_delimiter.join(int_parts), num_parts[1]])
    if is_negative:
        res = '-' + res
    return res
