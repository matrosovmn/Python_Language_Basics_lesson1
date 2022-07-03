my_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
new_rating = int(input("Введите новый элемент рейтинга в виде целого числа: "))
i = 0
for el in my_list:
    if new_rating <= el:
        i += 1

my_list.insert(i, new_rating)
print(my_list)