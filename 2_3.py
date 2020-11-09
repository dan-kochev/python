# задание_3
num = int(input("Введите месяц  в виде целого числа от 1 до 12: "))

# решение через dict
seasons = {'зима': [1, 2, 12],
           'весна': [3, 4, 5],
           'лето': [6, 7, 8],
           'осень': [9, 10, 11]}
for season, months in seasons.items():
    if num in months:
        print(f'Это {season}!')

# решение через list
months_seasons = [[1, 2, 12], 'зима', [3, 4, 5], 'весна', [6, 7, 8], 'лето', [9, 10, 11], 'осень']
for value in range(len(months_seasons)):
    if type(months_seasons[value]) == list:
        if num in months_seasons[value]:
            print(f'Это {months_seasons[value + 1]}!')
