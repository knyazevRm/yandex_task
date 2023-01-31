# Сильная цифра
# Давайте попробуем выполнить ещё одно простое действие — найдём максимальную цифру числа.
#
# Формат ввода
# Вводится одно натуральное число.
#
# Формат вывода
# Требуется вывести одно натуральное число — максимальную цифру исходного.


def max_digit_in_num(num):
    max_digit = num % 10
    while num != 0:
        max_digit = max(num % 10, max_digit)
        num //= 10

    return max_digit


if __name__ == '__main__':
    num = int(input())
    print(max_digit_in_num(num))
