class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Pen drawing')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Pencil drawing')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Handle drawing')
