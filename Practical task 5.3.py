with open('5.3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя заработная плата = {round(sum(employees_dict.values()) / len(employees_dict), 2)}\n'   # 3 - в функции round, кол-во знаков после округления - 0 это 1 и т.д.
          f'Сотрудники со средней заработной платой более 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')