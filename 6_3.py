# задание_3


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


engineer = Position('Андрей', 'Молотов', 'Engineer', 50000, 10000)
print(f'ФИО: {engineer.get_full_name()}, доход: {engineer.get_total_income()} тыс. руб.')
builder = Position('Олег', 'Петров', 'builder', 30000, 5000)
print(f'ФИО: {builder.get_full_name()}, доход: {builder.get_total_income()} тыс. руб.')
