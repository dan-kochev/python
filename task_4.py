# задание_4
number = int(input("Введите целое положительное число: "))
max_num = 0

while number > 0:
    if number % 10 > max_num:
        max_num = number % 10
    number = number // 10

print(f"Самая большая цифра в числе: {max_num}")
