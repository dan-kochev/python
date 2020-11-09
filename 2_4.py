# задание_4
words = input("Введите слова через пробел: ")
words = words.split()

for number, word in enumerate(words, 1):
    print(number, word[0:10])
