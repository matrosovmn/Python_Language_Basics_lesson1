class Warehouse:
    dict_tech = {}

    def take_tech(self, new_tech, tech_name, quantity_tech):
        prom_dict = {}
        if new_tech in self.dict_tech.keys() and tech_name in self.dict_tech[new_tech].keys():
            self.dict_tech[new_tech][tech_name] = self.dict_tech[new_tech][tech_name] + quantity_tech
            return self.dict_tech

        elif new_tech in self.dict_tech.keys() and tech_name not in self.dict_tech[new_tech].keys():
            prom_dict = {tech_name: quantity_tech}
            self.dict_tech[new_tech].update(prom_dict)
            return self.dict_tech



        else:
            prom_dict = {}
            prom_dict[tech_name] = quantity_tech

            self.dict_tech[new_tech] = prom_dict
            c = 1
            return self.dict_tech

    def give_tech(self, org_name, tech_type, tech_name, quantity_tech):
        if tech_type in self.dict_tech.keys() and quantity_tech <= self.dict_tech[tech_type][tech_name]:
            self.dict_tech[tech_type][tech_name] = self.dict_tech[tech_type][tech_name] - quantity_tech
            print(f'{org_name} получила {quantity_tech} единицы техники типа {tech_type}')

            return self.dict_tech
        else:
            return "Товар закончился!"


class Technics:
    type_tech = ''

    def __init__(self, name, mass, count, size: str):
        self.name = name
        self.mass = mass
        self.count = count
        self.size = size


class Printer(Technics):
    def __init__(self, name, mass, count, size, type):
        super().__init__(name, mass, count, size)
        self.type_tech = 'Принтер'
        self.type = type


class Scanner(Technics):
    def __init__(self, name, mass, count, size, resolution):
        super().__init__(name, mass, count, size)
        self.type_tech = 'Сканер'
        self.resolution = resolution


class Xerox(Technics):
    def __init__(self, name, mass, count, size, copy_speed):
        super().__init__(name, mass, count, size)
        self.type_tech = 'Ксерокс'
        self.copy_speed = copy_speed


def create_tech():
    dict_type_tech = {1: Printer, 2: Scanner, 3: Xerox}
    dict_dop_param = {1: 'Введите тип принтера: ', 2: 'Введите разрешение сканера: ',
                      3: 'Введите скорость копирования сканера: '}
    user_choice = int(input('Какую технику вы желаете сдать на склад?\n'
                            '1 - Принтер\n2 - сканер\n3 - ксерокс\n: '))
    name = input('Введите название техники: ')

    try:
        mass = int(input('Введите массу техники: '))
    except TypeError as err:
        print(f'Вводимые данные должны быть числом!{err} установлено дефолтное значение равное 1 ')

    try:
        count = int(input('Введите стоимость: '))
    except TypeError as err:
        print(f'Вводимые данные должны быть числом!{err} установлено дефолтное значение равное 1 ')

    size = input('Введите размеры техники (mm x mm) : ')
    dop_param = input(dict_dop_param[user_choice])
    new_tech = dict_type_tech[user_choice](name, mass, count, size, dop_param)
    return new_tech


def beautiful_list(warehouse_dict):
    print('Список техники на складе: ')
    for key_1 in warehouse_dict:
        beautiful_list = []
        for key_2, item in warehouse_dict[key_1].items():
            beautiful_list.append("{}: {} шт.".format(key_2.capitalize(), item))
        print(f'Тип техники: {key_1}\n{"; ".join(beautiful_list)}')


warehouse = Warehouse()
end = ''
while True:
    a = create_tech()
    quantity_tech = int(input(f'Сколько единиц техники типа {a.type_tech} вы хотите сдать на склад?: '))
    warehouse.take_tech(a.type_tech, a.name, quantity_tech)
    end = input('Если вся техника сдлана на склад, нажмите q, в противном случае нажмите enter: ')
    if end.lower() == 'q':
        break


def tech_in_warehouse():
    dict_type_tech = {1: 'Принтер', 2: 'Сканер', 3: 'Ксерокс'}
    beautiful_ls = []
    user_choise = int(input('Какую технику вы желаете забрать со склада?\n'
                            '1 - Принтер\n2 - сканер\n3 - ксерокс\n: '))
    if dict_type_tech[user_choise] in warehouse.dict_tech.keys():
        for key, item in warehouse.dict_tech[dict_type_tech[user_choise]].items():
            beautiful_ls.append("{}: {} шт.".format(key.capitalize(), item))
        print(f'В наличии:\n{"; ".join(beautiful_ls)}')
        return dict_type_tech[user_choise]
    else:
        print('Техники нет в наличии')


def tech_request():
    org_name = input('Введите название организации: ')
    tech_type = tech_in_warehouse()
    if tech_type != None:
        tech_name = input('Введите название техники: ')
        quantity_tech = int(input('Сколько единиц техники вы желаете забрать?: '))
        return warehouse.give_tech(org_name, tech_type, tech_name, quantity_tech)


while True:
    beautiful_list(warehouse.dict_tech)
    tech_request()
    end = input('Если желаете завершить программу, нажмите q, в противном случае нажмите Enter: ')
    if end.lower() == 'q':
        break

print('Программа завершена')
