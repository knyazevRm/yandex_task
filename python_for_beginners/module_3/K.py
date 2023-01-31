# Цифровая сумма
# Иногда требуется манипулировать с цифрами чисел.
# Одно из самых простых действий, которое можно совершить — найти сумму цифр числа.
# Напишите программу, чтобы выполнить это действие.
#
# Формат ввода
# Вводится одно натуральное число.
#
# Формат вывода
# Требуется вывести одно натуральное число — сумму цифр исходного.


def suma_of_digit(number):
    suma = 0
    while number != 0:
        suma += number % 10
        number //= 10

    return suma


if __name__ == '__main__':
    num = int(input())
    print(suma_of_digit(num))
