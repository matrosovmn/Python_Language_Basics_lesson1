def my_sum():
    sum_res = 0
    while True:
        number = input("Введите числа через пробел или Q для выхода из программы: ").split()
        for el in number:
            if el == "q" or el == "Q":
                return sum_res
            else:
                try:
                    sum_res = sum_res + + int(el)
                except ValueError:
                    print("Для выхода из программы нажмите Q: ")
        print(f"Сумма чисел {sum_res}")


print(my_sum())
