from sys import argv


def salary():
    try:
        time = float(input("Выработка в часах :"))
        rate = int(input("Ставка за час :"))
        bonus = int(input("Премия :"))
        res = time * rate + bonus
        print(f"заработная плата сотрудника  - {res}")
    except ValueError:
        print("Введите 3 числа")


salary()
