from itertools import count, cycle

print("Итератор, генерирующий целые числа, начиная с указанного. Для генерации след. числа нажмите Enter, для выхода нажмите q")
for el in count(int(input("Введите стартовое число :"))):
    print(el, end=" ")
    quit = input()
    if el == 10 or quit == "q":
        break

# print("Итератор, повторяющий элементы списка. Для генерации след. элемента нажмите Enter, для выхода нажмите q")
# my_list = input("Введите элементы списка через пробел :").split()
# el = cycle(my_list)
#
# while quit != "q":
#     print(next(el), end=" ")
#     quit = input()
