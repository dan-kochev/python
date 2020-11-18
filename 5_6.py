# задание_6

my_dict = {}

with open("5_6.txt") as f_obj:
    for line in f_obj:
        content = line.replace("(", " ").split()
        my_dict[content[0]] = sum(int(i) for i in content if i.isdigit())

print(my_dict)
