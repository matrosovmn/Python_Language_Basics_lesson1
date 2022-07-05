def int_func(word):
    latin_letters = "qwertyuiopasdfghjklzxcvbnm"
    return word.title() if not set(word).difference(latin_letters) else False


words = input("Введите через пробел несколько слов маленькими латинскими буквами: ").split()
for el in words:
    result = int_func(el)
    if result:
        print(int_func(el), ' ')