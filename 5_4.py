# задание_4

ru_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}
my_list = []

with open("5_4.txt") as f_obj:
    for line in f_obj:
        key_dict = line.split("-")
        if key_dict[0] in ru_dict:
            my_list.append(ru_dict.get(key_dict[0]) + "-" + key_dict[1])

with open("new_file_5_4.txt", "w") as new_f_obj:
    new_f_obj.writelines(my_list)
