# задание_7

from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


for el in fact(int(input("Число: "))):
    print(el)
