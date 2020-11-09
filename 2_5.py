# задание_5
my_list = [7, 5, 3, 3, 2]
element = int(input("Введите новый элемент: "))
check = my_list.count(element)

if check > 0:
    ind = my_list.index(element)
    my_list.insert(ind + check, element)
else:
    for number in my_list:
        if element > number:
            ind = my_list.index(number)
            my_list.insert(ind, element)
            break
        elif element < my_list[-1]:
            my_list.append(element)
print(my_list)
