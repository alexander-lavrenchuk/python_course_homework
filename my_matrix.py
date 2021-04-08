from format_num import *


def num_fix_format(num, fix_places):
    return str(num) if len(str(abs(num))) <= fix_places else f'{num:.2e}'


class Matrix:
    print_fix_places = 9

    def __init__(self, list_of_list):
        try:
            self.elements = list_of_list.copy()
        except AttributeError:
            self.elements = []

    def __str__(self):
        dbc = u'\u2551'  # Double vertical line symbol
        # Determining maximum width of each column
        max_width = []
        for c in range(len(self.elements[0])):
            max_width.append(0)
            for r in range(len(self.elements)):
                max_width[c] = max(max_width[c], len(format_num(self.elements[r][c], Matrix.print_fix_places)))

        # Composing multiline string with matrix elements
        res = ''
        for i in range(len(self.elements)):
            res += dbc
            row = []
            for j in range(len(self.elements[i])):
                el_str = format_num(self.elements[i][j], Matrix.print_fix_places)
                row.append(f'{el_str:>{max_width[j]}}')
            res += '; '.join(row)
            res += dbc + '\n'
        return res

    @property
    def size(self):
        return (len(self.elements), len(self.elements[0]))

    def __add__(self, other):
        if type(other) != type(self):
            print(f'Type of second addendum is {type(other)}, but should be {type(self)}.')
            return None
        if self.size != other.size:
            print('Matrices should be the same size to sum them up.')
            return None
        res = []
        for i in range(len(self.elements)):
            res.append([])
            for j in range(len(self.elements[i])):
                res[i].append(self.elements[i][j] + other.elements[i][j])
        res = Matrix(res)
        return res
