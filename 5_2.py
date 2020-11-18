# задание_2

with open("5_2.txt") as f_obj:
    lines = 0
    my_list = []
    for line in f_obj:
        lines += 1
        my_list.append(f'Строка {lines} - количество слов: {len(line.split())}')

print(f'Всего строк: {lines}')
for str_words in my_list:
    print(str_words)
