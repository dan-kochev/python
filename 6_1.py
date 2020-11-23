# задание_1

import time


class TrafficLight:
    __color = ("Красный", "Желтый", "Зеленый")

    def running(self):
        while True:
            for i in self.__color:
                if i == "Красный":
                    print(i)
                    time.sleep(7)
                elif i == "Желтый":
                    print(i)
                    time.sleep(2)
                elif i == "Зеленый":
                    print(i)
                    time.sleep(7)


colors = TrafficLight()
colors.running()
