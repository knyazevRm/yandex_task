# Красота спасёт мир
# Одно из древних поверий гласит, что трёхзначное число красиво,
# если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.
#
# Напишите систему определяющую красоту числа.
#
# Формат ввода
# Одно трёхзначное число
#
# Формат вывода
# YES — если число красивое, иначе — NO


def check_number(num):
    str_of_num = str(num)
    num_of_hundreds = int(str_of_num[0])
    num_of_tens = int(str_of_num[1])
    junior_category = int(str_of_num[2])

    max_digit = max(junior_category, num_of_tens, num_of_hundreds)
    min_digit = min(junior_category, num_of_tens, num_of_hundreds)

    return (sum([junior_category, num_of_tens, num_of_hundreds]) - min_digit - max_digit) * 2 == min_digit + max_digit


if __name__ == '__main__':
    number = int(input())

    if check_number(number):
        print("YES")
    else:
        print("NO")