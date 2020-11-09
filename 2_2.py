# задание_2
elements = list(input("Введите элементы: "))
length = len(elements)

for value in range(1, length, 2):
    elements[value - 1], elements[value] = elements[value], elements[value - 1]
print(''.join(elements))
