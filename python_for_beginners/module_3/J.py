# Маршрут построен
# Навигация была важна во все времена.
# Нам достался архив маршрутов движения,
# но их оказалось так много, что без автоматизации мы с ними не справимся во век.
# Каждый маршрут представляет собой последовательность шагов
# в одном из четырех направлений: * СЕВЕР; * ВОСТОК; * ЮГ; * ЗАПАД.
#
# Напишите программу, чтобы по заданному маршруту она определяла, в какой именно точке мы окажемся.
# Для простоты будем считать, что в начале маршрута мы находимся в точке (0; 0).
#
# Формат ввода
# Вводятся инструкции маршрута в виде:
# <направление>
# <количество шагов>
# Ввод завершается строкой СТОП.
#
# Формат вывода
# Два целых числа — координаты конечной точки маршрута.


class Point:
    def __init__(self, x, y):
        self.__x: int = x
        self.__y: int = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x += x

    @y.setter
    def y(self, y):
        self.__y += y

    def __str__(self):
        return f"{self.__y}\n{self.__x}"


def coordinate_offset(curr_coordinate: Point, direction: str, len: int):
    match direction:
        case "СЕВЕР":
            curr_coordinate.y = len
        case "ЮГ":
            curr_coordinate.y = -len
        case "ВОСТОК":
            curr_coordinate.x = len
        case "ЗАПАД":
            curr_coordinate.x = -len


if __name__ == '__main__':
    point = Point(0, 0)

    while (direction := input()) != "СТОП":
        coordinate_offset(point, direction, int(input()))

    print(point)
