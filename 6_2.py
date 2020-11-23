# задание_2


class Road:

    mass = None
    thickness = None

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def weight(self):
        self.thickness = 0.05  # (м) толщина полотна
        self.mass = 25  # (кг) масса асфальта для покрытия одного квадратного метра толщиной в 1 см
        print(f'Потребуется: {self._length * self._width * self.mass * self.thickness / 1000} т асфальта')


road_test = Road(2000, 10)
road_test.weight()
