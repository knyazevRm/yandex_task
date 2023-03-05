# Простая задача 2.0
# В банке решили переписать программу для шифрования данных и попросили,
# чтобы вы взяли на себя часть данной задачи.
# Напишите программу для разложения числа на простые множители.
# Только внимательно, ведь работать придётся вновь с простыми числами.
#
# Формат ввода
# Вводится одно натуральное число.
#
# Формат вывода
# Требуется составить математическое выражение — произведение простых неубывающих чисел,
# которое в результате даёт исходное.


def factorize(num):
    result = []
    d = 2
    while d ** 2 <= num:
        if num % d == 0:
            result.append(d)
            num //= d
        else:
            d += 1

    if num != 1:
        result.append(num)

    return result


def print_result(array):
    length = len(array)
    for i in range(length - 1):
        print(f"{array[i]} *", end=" ")

    print(array[length - 1])


if __name__ == '__main__':
    number = int(input())
    print_result(factorize(number))
