#  Корень зла
# Не все любят математику, а кто-то даже считает её настоящим злом во плоти,
# хотя от неё никуда не деться. К примеру, Python изначально разрабатывался только для решения математических задач,
# поэтому давайте используем его, чтобы найти корни квадратного уравнения.

# Формат ввода
# Вводится 3 вещественных числа
# a, b, c — коэффициенты уравнения вида:

# Формат вывода
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».
#
# Примечание
# Обратите внимание, что ограничения на значения коэффициентов отсутствуют.


def get_answer(num: float):
    if num.is_integer():
        return f"{int(num)}.00"

    return num


def get_route(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite solutions"

            return "No solution"
        else:
            return get_answer(round(- c / b, 2))

    discriminant = b ** 2 - 4 * a * c

    if discriminant == 0:
        return get_answer(round(- b / (2 * a), 2))
    elif discriminant > 0:
        x_1 = round((- b - discriminant ** .5) / (2 * a), 2)
        x_2 = round((- b + discriminant ** .5) / (2 * a), 2)

        return f"{get_answer(min(x_1, x_2))} {get_answer(max(x_1, x_2))}"

    return "No solution"


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())

    print(get_route(a, b, c))