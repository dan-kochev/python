# задание_6
distance_begin = float(input("В первый день спортсмен пробежал (км): "))
distance_end = float(input("Цель спортсмена (км): "))
day = 1

while distance_begin < distance_end:
    distance_begin += distance_begin * 0.1
    day += 1

print(f"Спортсмен достигнет цели в {day} день.")