# задание_3


def my_func(arg_1, arg_2, arg_3):
    """Возвращает сумму наибольших двух элементов"""
    args = [arg_1, arg_2, arg_3]
    args.remove(min(args))
    return sum(args)


print(my_func(int(input("Первый аргумент: ")), int(input("Второй аргумент: ")), int(input("Третий аргумент: "))))
