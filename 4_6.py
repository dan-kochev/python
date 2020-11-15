# задание_6

from itertools import count
from itertools import cycle

# а) итератор, генерирующий целые числа, начиная с указанного:


def int_iterator(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)


int_iterator(3, 10)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее:


def cycle_iterator(colors, repeat):
    i = 1
    for color in cycle(colors):
        if i > repeat:
            break
        print(color)
        i += 1


cycle_iterator(['зеленый', 'желтый', 'красный', 'желтый'], 5)
