while True:
    def division_numbers(*args):
        try:
            number1 = float(input("Введите число 1 : "))
            number2 = float(input("Введите число 2, отличное от нуля : "))
            result = number1 / number2
        except ValueError:
            return "Введены некорректные данные"
        except ZeroDivisionError:
            return "Деление на ноль невозможно"
        return result
    print(f"Результат деления - {division_numbers()}")
    # break
