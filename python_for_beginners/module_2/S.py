# Автоматизация безопасности
# Группа исследователей собирается высадиться на остров невероятно ровной формы,
# но разведка при помощи спутника выяснила, что на острове есть зона зыбучих песков.
#
# Для повышения безопасности экспедиции было решено разработать систему оповещения,
# которая предупредит исследователей об опасности.
# А для снижения расходов на производство было решено заказать программное обеспечение.


class Figure:
    def __init__(self, left, right, point):
        self.left = left
        self.right = right
        self.point = point

    def check_boundary(self):
        return self.left <= self.point.x <= self.right

    def func(self):
        pass

    def include(self):
        pass


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Line(Figure):
    def __init__(self, k, c, left, right, point):
        super().__init__(left, right, point)
        self.k = k
        self.c = c

    def func(self):
        return self.k * self.point.x + self.c

    def include(self):
        if self.check_boundary():
            return self.func() >= self.point.y

        return False


class Circle(Figure):
    def __init__(self, a, b, r, left, right, point):
        super().__init__(left, right, point)
        self.a = a
        self.b = b
        self.r = r

    def func(self):
        return (self.point.x - self.a) ** 2 + (self.point.y - self.b) ** 2

    def include(self):
        if self.check_boundary():
            return self.func() <= self.r ** 2

        return False


class Parabola(Figure):
    def __init__(self, a, b, c, left, right, point):
        super().__init__(left, right, point)
        self.a = a
        self.b = b
        self.c = c

    def func(self):
        return self.a * self.point.x ** 2 + self.b * self.point.x + self.c

    def include(self):
        if self.check_boundary():
            return self.point.y <= self.func()

        return False


def check_zone(point):
    list_of_dangerous_figure = [Line(k=5 / 3, c=35 / 3, left=-7, right=-4, point=point),
                                Line(k=0, c=5, left=-4, right=0, point=point),
                                Circle(a=0, b=0, r=5, left=0, right=5, point=point),
                                Parabola(a=.25, b=.5, c=-8.5, left=-7, right=5, point=point)]

    save_figure = Circle(a=0, b=0, r=10, left=-10, right=10, point=point)

    for figure in list_of_dangerous_figure:
        if figure.include():
            return "Dangerous"

    if save_figure.include():
        return "Save"

    return "Out"


def main(point):
    match check_zone(point):
        case "Dangerous":
            print("Опасность! Покиньте зону как можно скорее!")
        case "Save":
            print("Зона безопасна. Продолжайте работу.")
        case "Out":
            print("Вы вышли в море и рискуете быть съеденным акулой!")


if __name__ == '__main__':
    x = float(input())
    y = float(input())

    point = Point(x, y)

    main(point)
