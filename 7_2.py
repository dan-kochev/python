# задание_2

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, option):
        self.option = option

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return f'{(self.option / 6.5) + 0.5:.2f}'


class Suit(Clothes):
    @property
    def calculate(self):
        return f'{(2 * self.option) + 0.3:.2f}'


coat = Coat(50)
suit = Suit(175)

print(coat.calculate)
print(suit.calculate)
