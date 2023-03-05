# Максимальная сумма
# Ребята в детском саду снова играют с числами. И пусть числа они знают плохо,
# придумывать их они очень любят.
# Они договорились, что будут называть числа по очереди и тот,
# кто назовёт число с наибольшей суммой цифр, будет считаться победителем.
# В качестве судьи они выбрали бедную воспитательницу, и она попросила нас о помощи.
# Напишите программу, которая определит победителя.
#
# Формат ввода
# В первой строке записано число
# N — количество детей в группе. Далее вводятся имя ребенка и его число (каждое на своей строке).
#
# Формат вывода
# Требуется вывести имя победителя.
# Если два ребенка назвали числа с одинаковой суммой цифр, победителем должен быть признан тот, кто ходил позже.


def get_sum_of_digit(num):
    suma = 0
    while num != 0:
        suma += num % 10
        num //= 10

    return suma


def get_index_of_max(numbers):
    max_index = 0
    max_value = get_sum_of_digit(numbers[max_index])

    for i in range(1, len(numbers)):
        if (tmp := get_sum_of_digit(numbers[i])) >= max_value:
            max_index = i
            max_value = tmp

    return max_index


if __name__ == '__main__':
    num = int(input())
    names = list()
    numbers = list()

    for i in range(num):
        names.append(input())
        numbers.append(int(input()))

    print(names[get_index_of_max(numbers)])