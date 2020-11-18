# задание_1

text = []
while True:
    line = input("Введите текст: ")
    if line == '':
        print(text)
        break
    else:
        new_line = line + "\n"
        text.append(new_line)

with open("5_1.txt", "w") as f_obj:
    f_obj.writelines(text)
