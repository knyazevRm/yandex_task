# Властелин Чисел: Возвращение Цезаря
# До победы над злом остался один шаг — разрушить логово Зерона.
#
# Для этого нужно создать трёхзначное магическое число,
# которое будет сильнее двух двухзначных защитных чисел Зерона.
#
# Самый простой способ создать сильное число:
#
# первой взять максимальную цифру из всех защитных чисел;
# последней — минимальную;
# в середину поставить сумму оставшихся без учёта переноса разряда.
# Помогите одолеть зло.
#
# Формат ввода
# В двух строках записаны защитные числа Зерона.
#
# Формат вывода
# Одно трёхзначное число, которое приведёт к победе.


def create_magic_numbers(num_a, num_b):
    num_a_tens = num_a // 10
    num_a_ones = num_a % 10

    num_b_tens = num_b // 10
    num_b_ones = num_b % 10

    sum_of_digit = sum([num_a_ones, num_b_ones, num_a_tens, num_b_tens])

    max_digit = max(num_a_ones, num_b_ones, num_a_tens, num_b_tens)
    min_digit = min(num_a_ones, num_b_ones, num_a_tens, num_b_tens)

    return f"{max_digit}{(sum_of_digit - min_digit - max_digit) % 10}{min_digit}"


if __name__ == '__main__':
    first_num = int(input())
    second_num = int(input())

    print(create_magic_numbers(first_num, second_num))