# задание_1


def division(num_1, num_2):
    """Выполняет деление двух чисел."""
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


print(division(int(input("Первое число: ")), int(input("Второе число: "))))
