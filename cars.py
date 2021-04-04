class Car:
    def __init__(self, name, color, speed=None, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'The car {self.name} has started driving.')

    def stop(self):
        print(f'The car {self.name} has stopped.')

    def turn(self, direction):
        print(f'The car {self.name} has turned {direction}.')

    def show_speed(self):
        print(f'The car {self.name} has speed {self.speed} km/h.')

    def show_police_type(self):
        if self.is_police:
            print(f'The car {self.name} is a police car.')
        else:
            print(f'The car {self.name} is not a police car.')


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            print(f'The TownCar {self.name} has speed {self.speed} km/h, exceeds the speed limit {speed_limit} km/h.')
        else:
            print(f'The TownCar {self.name} has speed {self.speed} km/h.')


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        speed_limit = 40
        if self.speed > speed_limit:
            print(f'The WorkCar {self.name} has speed {self.speed} km/h, exceeds the speed limit {speed_limit} km/h.')
        else:
            print(f'The WorkCar {self.name} has speed {self.speed} km/h.')


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, is_police=True)
