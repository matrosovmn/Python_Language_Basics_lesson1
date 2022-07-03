def my_func(*args):
    args1 = int(input("Введите целое число 1 : "))
    args2 = int(input("Введите целое число 2 :"))
    args3 = int(input("Введите целое число 3 :"))

    if args1 >= args2 > args3:
        return args1 + args2
    elif args2 >= args1 > args3:
        return args2 + args1
    elif args3 >= args2 > args1:
        return args3 + args2
    elif args3 >= args1 > args2:
        return args3 + args1
    elif args1 >= args3 > args2:
        return args1 + args3
    elif args2 >= args3 > args1:
        return args2 + args3
    # else:
    #     exit(1)


print(f"Cумма наибольших двух введенных чисел : {my_func()}")
