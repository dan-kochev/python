# задание_1

from sys import argv


def wage_func(output, rate, bonus):
    """Рассчитывает размер заработной платы"""
    return (output * rate) + bonus


param_1, param_2, param_3, param_4 = argv

print(f'Имя скрипта: {param_1}')
print(f'Выработка: {param_2} ч.')
print(f'Ставка: {param_3} руб/час')
print(f'Премия: {param_4} рублей')
print('*' * 30)
print(f' Заработная плата: {wage_func(int(param_2), int(param_3), int(param_4))} рублей')
