from abc import abstractmethod


class Clothes:
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __str__(self):
        return str(self.param)

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Suit(Clothes):

    @property
    def consumption(self):
        return round(self.param * 2) + 0.3


V = Coat(50)
H = Suit(1.74)

print(f'Расход ткани для пальто - {V.consumption}')
print(f'Расход ткани для костюма - {H.consumption}')
print(f'Общий расход ткани - {V+H}')
