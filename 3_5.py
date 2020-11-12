# задание_5


def sum_num():
    """Находит сумму чисел, введенных в строку через пробел"""
    total_result = 0
    out = ''
    while out != "q":
        text = input("Введите числа или нажмите q для выхода: ").split()
        result = 0
        for symbol in range(len(text)):
            if text[symbol].lower() == 'q':
                out = "q"
                break
            else:
                result += float(text[symbol])
        total_result += result
        print(f'Промежуточный итог равен: {total_result}')
    print(f'Общийитог равен: {total_result}')


sum_num()
