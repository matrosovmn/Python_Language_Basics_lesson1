class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {"Оклад": wage, "Премия": bonus}

    @property
    def position(self):
        return self._position


class Position(Worker):
    def get_full_name(self):
        return f"{self._name} {self._surname}"

    def get_total_income(self):
        return f'{sum(self._income.values())}'


employee = Position('Иван', 'Леснов', 'Менеджер', 1000, 500)
print(employee.get_full_name())
print(employee.position)
print(employee.get_total_income())
