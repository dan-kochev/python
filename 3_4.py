# задание_4


def my_func(x, y):  # Возведение в степень с помощью оператора **
    return 1 / x ** abs(y)


print(my_func(float(input("Дейтсвительное положительное число: ")), int(input("Целое отрицательное: "))))


def my_function(a, b):  # Возведение в степень с помощью цикла while
    b = abs(b)
    result = 1
    while b > 0:
        result *= a
        b -= 1

    return 1 / result


print(my_function(float(input("Дейтсвительное положительное число: ")), int(input("Целое отрицательное: "))))
