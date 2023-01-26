# Властелин Чисел: Две Башни
# Во времена, когда люди верили в великую силу чисел, оказалось,
# что волшебник Пифуман предал все народы и стал помогать Зерону.
#
# Чтобы посетить башни обоих злодеев одновременно,
# нам следует разделить магию числа, которое защищало нас в дороге.
#
# Чтобы поделить трёхзначное число,
# нам нужно составить из него минимально и максимально возможные двухзначные числа.
#
# Формат ввода
# Одно трёхзначное число.
#
# Формат вывода
# Два защитных числа для каждого отряда, записанные через пробел.


def create_two_numbers(num):
    str_of_num = str(num)
    num_of_hundreds = int(str_of_num[0])
    num_of_tens = int(str_of_num[1])
    junior_category = int(str_of_num[2])

    max_digit = max(num_of_hundreds, num_of_tens, junior_category)
    min_digit = min(num_of_hundreds, num_of_tens, junior_category)
    average_digit = sum([num_of_hundreds, num_of_tens, junior_category]) - min_digit - max_digit

    if min_digit == 0:
        return f"{average_digit}{min_digit} {max_digit}{average_digit}"

    return f"{min_digit}{average_digit} {max_digit}{average_digit}"


if __name__ == '__main__':
    numbers = int(input())

    print(create_two_numbers(numbers))