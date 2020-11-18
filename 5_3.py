# задание_3

with open("5_3.txt") as f_obj:
    my_list = []
    sum_wages = 0
    staff = 0
    for line in f_obj:
        my_str = line.split()
        if float(my_str[1]) < 20000.00:
            my_list.append(my_str[0])
            sum_wages += float(my_str[1])
            staff += 1
print(f'Оклад менее 20 тыс. рублей имеют сотрудники: ')
for ind, surname in enumerate(my_list, 1):
    print(ind, surname)
print(f'Средняя величина дохода этих сотрудников составляет: {sum_wages / staff:.2f} рублей')
