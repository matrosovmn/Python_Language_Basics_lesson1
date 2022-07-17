class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return f"Масса асфальта, необходимого для покрытия дороги {self._length}м (длина) " \
               f"* {self._width}м (ширина) * 25 кг * 5 см = {(self._length * self._width * 25 * 5)/1000} тн"


road = Road(5000, 20)
print(road.mass())
