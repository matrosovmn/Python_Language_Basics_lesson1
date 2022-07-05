def my_func(*args):
    num1 = int(input("Введите целое число 1 : "))
    num2 = int(input("Введите целое число 2 : "))
    num3 = int(input("Введите целое число 3 : "))

    if num1 >= num2 > num3:
        return num1 + num2
    elif num2 >= num1 > num3:
        return num2 + num1
    elif num3 >= num2 > num1:
        return num3 + num2
    elif num3 >= num1 > num2:
        return num3 + num1
    elif num1 >= num3 > num2:
        return num1 + num3
    elif num2 >= num3 > num1:
        return num2 + num3

print(f"Cумма наибольших двух введенных чисел : {my_func()}")
