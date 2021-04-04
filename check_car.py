"""
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""

from cars import *
john_town_car = TownCar("John's town car", 'black')
kate_town_car = TownCar("Kate's town car", 'green')
lee_sport_car = SportCar("Lee's sport car", 'red')
leo_work_car = WorkCar("Leo's work car", 'brown')
max_work_car = WorkCar("Max's work car", 'yellow')
suse_police_car = PoliceCar("Suse's police car", 'white and blue')

john_town_car.go()
john_town_car.turn('right')
john_town_car.stop()

john_town_car.show_police_type()
john_town_car.speed = 110
john_town_car.show_speed()

print('')
kate_town_car.show_police_type()
kate_town_car.speed = 55
kate_town_car.show_speed()

print('')
lee_sport_car.show_police_type()
lee_sport_car.speed = 170
lee_sport_car.show_speed()

print('')
leo_work_car.show_police_type()
leo_work_car.speed = 35
leo_work_car.show_speed()

print('')
max_work_car.show_police_type()
max_work_car.speed = 55
max_work_car.show_speed()

print('')
suse_police_car.show_police_type()
suse_police_car.speed = 90
suse_police_car.show_speed()
