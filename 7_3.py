# задание_3


class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, ranks):
        return '\n'.join(['*' * ranks for _ in range(self.num // ranks)]) + '\n' + '*' * (self.num % ranks)

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return f'Объединение клеток. Число ячеек новой клетки: ' + str(self.num + other.num)

    def __sub__(self, other):
        if (self.num - other.num) > 0:
            return self.num - other.num
        else:
            return 'Вычитание клеток невозможно'

    def __mul__(self, other):
        return f'Умножение клеток. Число ячеек новой клетки: ' + str(self.num * other.num)

    def __truediv__(self, other):
        return f'Деление клеток. Число ячеек новой клетки: ' + str(round(self.num / other.num))


cell_1 = Cell(20)
cell_2 = Cell(40)

print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_2.make_order(15))
