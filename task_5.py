# задача_5
proceeds = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))

if proceeds > costs:
    print("Фирма работает с выручкой, причем: ")
    profitability = (proceeds - costs) / proceeds
    print(f"рентабельность выручки остсавляет {round(profitability, 2)}")
    employees = int(input("Введите количество сотрудников: "))
    profit_employees = (proceeds - costs) / employees
    print(f"Прибыль в расчете на одного сотрудника составляет: {round(profit_employees, 2)} рублей.")

elif proceeds == costs:
    print("Выручка равна издержкам, фирма работает с нулевой прибылью.")

else:
    print("Фирма работает в убыток.")
