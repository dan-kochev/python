# задание_6
goods = []
options = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
num = 0
out = ''

while out.lower() != "q":
    num += 1
    for i in options.keys():
        option = input(f'Введите такую характеристику товара, как {i}: ')
        if i == 'цена' or i == 'количество':
            options[i] = int(option)
        else:
            options[i] = option
        analytics[i].append(options[i])
    goods.append((num, options))
    out = input("Для продолжения нажмите Enter; чтобы выйти нажмите q: ")

print("Аналитика по товарам: ")
for key, value in analytics.items():
    print(f'{key}: {value}')
