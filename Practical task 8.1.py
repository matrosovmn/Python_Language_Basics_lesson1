class Data:


    def __init__(self, data_str):
        self.data_str = data_str

    def change_str(self):
        self.data_str = self.data_str.split('-')
        self.data_str = list(map(int, self.data_str))
        return self.data_str

    @staticmethod
    def cheсk_data(list_data):
        if list_data[2] % 4 == 0:
            res_check = 29
        else:
            res_check = 28
        dict_month_day = {1: 31, 2: res_check, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if list_data[1] not in dict_month_day.keys():
            return 'Не верный формат даты '
        if not (list_data[0] <= dict_month_day[list_data[1]] and list_data[0] > 0):
            return 'Неверный формат даты '
        return 'Формат даты правильный'


data = Data(input('Введите дату в формате: день-месяц-год '))
a = data.change_str()
print(data.cheсk_data(a))
