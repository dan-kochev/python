# лото

from random import randint
from time import sleep


class Card:
    def __init__(self):
        numbers = self.random_numbers(1, 90, 15)
        self.card = {}
        for row in range(1, 4):
            numbers_str = self.random_numbers(1, 9, 5, True)
            self.card.update({num: [True, row, col] for num, col in
                              zip(sorted(numbers[(row - 1) * 5:(row - 1) * 5 + 5]), numbers_str)})

    def __str__(self):
        field = 4
        single_str = '-' * (9 * (field + 1) + 1) + '\n'
        out_str = single_str
        for row in range(1, 4):
            out_str += '|'
            for col in range(1, 10):
                num_check = self.__num_search(row, col)
                if num_check != None:
                    if num_check[1]:
                        str_check = str(num_check[0])
                    else:
                        str_check = '(' + str(num_check[0]) + ')'
                else:
                    str_check = ''
                out_str += str(str_check.center(field)) + '|'
            out_str += '\n' + single_str
        return out_str

    def num_in_card(self, num):
        if self.card.get(num) == None:
            return False
        else:
            self.card[num][0] = False
            return True

    def card_is_finish(self):
        return True if sum(1 in x for x in self.card.values() if x[0]) == 0 else False

    @staticmethod
    def random_numbers(low_range, hi_range, amount, sort=False):
        my_set = set()
        while len(my_set) < amount:
            my_set.add(randint(low_range, hi_range))
        my_list = sorted(list(my_set)) if sort else list(my_set)
        return my_list

    def __num_search(self, row, col):
        for key, val in self.card.items():
            if val[1] == row and val[2] == col:
                return (key, val[0])
        return None


def yes_no_dialog(question, default_answer="yes"):
    answers = {"yes": 1, "y": 1, "ye": 1,
               "no": 0, "n": 0}
    if default_answer == None:
        tip = " [y/n] "
    elif default_answer == "yes":
        tip = " [y/n] "
    elif default_answer == "no":
        tip = " [y/n] "
    else:
        raise ValueError(f'Неверное значение: {default_answer = }')
    while True:
        print(question + tip + ": ", end="")
        user_answer = input().lower()
        if default_answer is not None and user_answer == '':
            return answers[default_answer]
        elif user_answer in answers:
            return answers[user_answer]
        else:
            print("Пожалуйста, введите yes/y или no/n\n")


my_card = Card()
pc_card = Card()
num_list = [i for i in range(1, 91)]
pc_card_change = my_card_change = True
while len(num_list):
    if pc_card_change or my_card_change:
        print('Ваша карточка:\n', my_card)
        print('Карточка компьютера:\n', pc_card)
        if my_card.card_is_finish():
            print('Вы выиграли!')
            break
        if pc_card.card_is_finish():
            print('Компьютер выиграл!')
            break
    num_check = num_list.pop(randint(0, len(num_list) - 1))
    pc_card_change = pc_card.num_in_card(num_check)
    my_card_change = my_card.num_in_card(num_check)
    my_answer = yes_no_dialog(f'На вашей карте есть цифра ({num_check})?', 'no')
    if my_answer == 1 and my_card_change == False or my_answer == 0 and my_card_change == True:
        print('Вы ошиблись и проиграли!')
        break
