# задание_7

import json

firm_dict = {}
profit_dict = {}
total_profit = 0
my_list = []
num_firm = 0

with open("5_7.txt") as f_obj:
    for line in f_obj:
        content = line.split()
        profit = int(content[2]) - int(content[3])
        firm_dict[content[0]] = profit
        if profit >= 0:
            total_profit += profit
            num_firm += 1

profit_dict = {"average_profit": total_profit // num_firm}
my_list.append(firm_dict)
my_list.append(profit_dict)

with open("5_7.json", "w") as write_f:
    json.dump(my_list, write_f)
