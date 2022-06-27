number = int(input("Введите целое положительное число : "))
max = number % 10

while number > 0:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    if number == 9:
        continue
    else:
        print("Максимальная цифра в числе :", max)
        break
