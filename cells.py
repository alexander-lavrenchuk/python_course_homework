class Cells:
    def __init__(self, cells_num):
        try:
            self.cells_num = int(cells_num)
        except ValueError:
            print('Initialization parameter should be an integer number.')
            self.cells_num = 0

    def __str__(self):
        return f'Cells number is {self.cells_num}.'

    def __add__(self, other):
        if type(self) != type(other):
            print(f"TypeError: can only sum up two objects of class Cells (not {type(self)} + {type(other)}).")
            return None
        return Cells(self.cells_num + other.cells_num)

    def __sub__(self, other):
        if type(self) != type(other):
            print(f"TypeError: can only subtract two objects of class Cells (not {type(self)} - {type(other)}).")
            return None
        elif self.cells_num <= other.cells_num:
            print('Minuend cell should contain more cells, than subtrahend cell.')
            return None
        return Cells(self.cells_num - other.cells_num)

    def __mul__(self, other):
        if type(self) != type(other):
            print(f"TypeError: can only multiply two objects of class Cells (not {type(self)} * {type(other)}).")
            return None
        return Cells(self.cells_num * other.cells_num)

    def __truediv__(self, other):
        if type(self) != type(other):
            print(f"TypeError: can only true divide two objects of class Cells (not {type(self)} / {type(other)}).")
            return None
        return Cells(self.cells_num // other.cells_num)

    def make_order(self, cells_num_in_row):
        try:
            cells_in_row = int(cells_num_in_row)
            if cells_in_row < 1:
                print("Method 'make_order' of class <class Cells> should take an integer parameter greater than 0.")
                order_str = ''
            else:
                order_str = ''
                for i in range(1, self.cells_num + 1):
                    order_str += '*'
                    if i % cells_num_in_row == 0:
                        order_str += '\n'
        except ValueError:
            print("Method 'make_order' of class <class Cells> should take an integer parameter.")
            order_str = ''
        return order_str
