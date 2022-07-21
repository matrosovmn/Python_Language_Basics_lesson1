class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите числитель: '))
b = int(input('Введите знаменатель: '))
try:
    if b == 0:
        raise MyError('Деление на ноль недопустимо')
except MyError as err:
    print(err)
else:
    res = a / b
    print(f'Результат деления: {round(res, 2)}')
