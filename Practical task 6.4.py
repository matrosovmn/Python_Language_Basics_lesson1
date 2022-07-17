class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Машина поехала'

    def stop(self):
        return f'{self.name} Машина остановилась'

    def turn_right(self):
        return f'{self.name} Машина повернула направо'

    def turn_left(self):
        return f'{self.name} Машина повернула налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name}  - превышение скорости!'
        else:
            return f'Скорость {self.name} - допустимая'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} - превышение скорости'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


Lamba = SportCar(200, 'Red', 'Lamba', False)
Toyota = TownCar(70, 'Black', 'Toyota', False)
KAMAZ = WorkCar(50, 'Orange', 'KAMAZ', False)
Reno_Logan = PoliceCar(120, 'White',  'Reno_Logan', True)
print(Lamba.turn_left())
print(f'Когда {Toyota.turn_right()} то {KAMAZ.stop()}')
print(f'{Toyota.go()} {Toyota.show_speed()}')
print(f'{Toyota.name} {Toyota.color}')
print(f'{Toyota.name} полицейская машина? {Toyota.is_police}')
print(f'{Reno_Logan.name}  полицейская машина? {Reno_Logan.is_police}')
print(Reno_Logan.police())
print(Reno_Logan.show_speed())