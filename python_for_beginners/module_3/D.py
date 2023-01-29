# Считалочка 2.0
# Дети продолжают запоминать цифры, а мы им помогать.
# Нам вновь называют начало и конец последовательности чисел, а мы выводим их и числа между.
#
# Формат ввода
# Два числа, каждое с новой строки.
#
# Формат вывода
# Все числа от начала до конца (включительно), записанные через пробел.


def get_range(first, last, step=1):
    return [i for i in range(first, last, step)]


if __name__ == '__main__':
    first = int(input())
    last = int(input())

    if first > last:
        last -= 1
    else:
        last += 1

    step = 1 if first < last else -1

    print(*get_range(first, last, step=step))
