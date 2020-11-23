# задание_5


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'{self.title} пишет.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'{self.title} рисует.')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'{self.title} выделяет.')


pen_test = Pen()
pencil_test = Pencil()
handle_test = Handle()

pen_test.draw()
pencil_test.draw()
handle_test.draw()
