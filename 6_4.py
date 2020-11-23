# задание_4


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил скорость!')
        else:
            print(f'Скорость автомобиля составляет: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Нарушитель! Автомобиль {self.name} превысил скорость!')
        else:
            print(f'Скорость автомобиля: {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


test_1 = TownCar(65, 'black', 'Mazda 6')
test_2 = SportCar(250, 'silver', 'Mitsubishi Lancer Evo 4')
test_3 = WorkCar(50, 'white', 'Gazelle Next')
test_4 = PoliceCar(90, 'white', 'Uaz Patriot')

test_1.go()
test_1.show_speed()
test_1.stop()
print(test_1.name)
print(test_1.color)

test_2.go()
test_2.turn('налево')

test_3.stop()
print(test_3.name)

test_4.show_speed()
