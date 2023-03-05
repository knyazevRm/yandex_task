# Чётная чистота
# Мы уже достаточно знатоки, чтобы очистить число от определённых цифр,
# поэтому давайте напишем программу, которая уберёт все чётные цифры из числа.
#
# Формат ввода
# Одно натуральное число.
#
# Формат вывода
# Одно натуральное число — результат очистки.


def number_without_even_digit(num):
    result = ""
    for i in range(len(num)):
        if int(num[i]) % 2 != 0:
            result += num[i]

    return int(result)


def main():
    num = input()
    print(number_without_even_digit(num))


if __name__ == '__main__':
    main()
