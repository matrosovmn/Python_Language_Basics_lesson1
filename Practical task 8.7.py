class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b >= 0:
            return f'{self.a} +{self.b}i'
        else:
            return f'{self.a} {self.b}i'

    def __add__(self, other):
        return f'Сумма комплексных чисел z1 и z2 равна: {Complex(self.a + other.a, self.b + other.b)}'

    def __mul__(self, other):
        return f'Произведение комплексных чисел z1 и z2 равно: {Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)}'


a1, b1 = list(map(int, input('Введите через пробел действительную и мнимую части первого числа(z1): ').split(' ')))
z_1 = Complex(a1, b1)
a2, b2 = list(map(int, input('Введите через пробел действительную и мнимую части второго числа(z2): ').split(' ')))
z_2 = Complex(a2, b2)
print(z_1 + z_2)
print(z_1 * z_2)
