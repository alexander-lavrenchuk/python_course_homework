def math_round(num, float_digs=2):
    sign = 1 if num >= 0 else -1
    num = abs(num)
    if num * 10 ** (float_digs + 1) % 10 >= 5:
        return sign * (int(num * 10 ** float_digs) + 1) / 10 ** float_digs
    return sign * (int(num * 10 ** float_digs)) / 10 ** float_digs
