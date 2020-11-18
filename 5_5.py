# задание_5

numbers = "101 102 103 104 105 106 107"

with open("5_5.txt", "w") as f_obj:
    f_obj.write(numbers)

with open("5_5.txt") as new_f_obj:
    content = new_f_obj.read()

sum_num = 0
for element in content.split():
    sum_num += int(element)

print(content)
print(f'Сумма чисел равна: {sum_num}')
