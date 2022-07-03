goods = []
structure = {"Название": " ", "Цена": '', "Кол-во": '', "Шт.": ''}
analytics = {"Название": [], "Цена": [], "Кол-во": [], "Шт.": []}
num = 0
while True:
    if input("Для выхода нажмите 'Q', для продолжения нажмите 'Enter' ").upper() == 'Q':
        break
    num += 1
    for el in structure.keys():
        product = input(f'Введите товар "{el}" - ')
        structure[el] = int(product) if (el == "Цена" or el == "Кол-во") else product
        analytics[el].append(structure[el])
    goods.append((num, structure.copy()))
    print(f"\nСтруктура товаров:\n{goods}")

    print(f"\nТекущая аналитика товаров:\n{'-' * 25}")
    for key, value in analytics.items():
        print(f'{key[:15]:>10}: {value}')
    print('-' * 25)
    break