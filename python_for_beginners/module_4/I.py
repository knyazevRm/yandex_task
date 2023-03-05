# Большое число
# Дети никак не успокоятся и продолжают «мучить» числа.
# Сейчас они хотят общими силами составить очень большое число.
# Каждый ребёнок называет число состоящее из цифр, которые он знает.
# Напишите программу, которая строит число,
# состоящее из максимальных цифр каждого ребёнка.
#
# Формат ввода
# В первой строке указано число
# N — количество детей в группе. В каждой из последующих
# N строк записано число.
#
# Формат вывода
# Одно большое число.


def max_digit_in_numbers(number):
    max_digit = number % 10
    number //= 10

    while number != 0:
        if max_digit < (tmp := number % 10):
            max_digit = tmp
        number //= 10

    return max_digit


if __name__ == '__main__':
    num = int(input())
    result = ""
    for i in range(num):
        result += str(max_digit_in_numbers(int(input())))

    print(result)