my_list = input("Введите нескольких слов, разделённых пробелами: ").split()
for el, word in enumerate(my_list, 1):
    print(f"{el}) {word[:10]}")