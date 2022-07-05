def my_func(x, y):
    x = x ** y
    y = 1
    i = 1
    while i <= abs(y):
        y *= x
        i += 1

    return x

print(
    my_func(
        int(input("Введите целое положительное число x: ")),
        int(input("Введите целое отрицательное число y: "))
    )
)
