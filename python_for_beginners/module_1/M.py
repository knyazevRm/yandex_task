# Дед Мороз и конфеты
# Настало самое главное событие в детском саду — новогодний утренник.
# Хорошо замаскированная робоняня в роли Деда Мороза решила раздать детям конфеты так,
# чтобы каждому досталось поровну. Напишите для робоняни алгоритм, который поможет распределить конфеты.
#
# Формат ввода
# В первой строке указано количество детей на утреннике.
# Во второй строке — количество конфет в конфетном отсеке робоняни.
#
# Формат вывода
# Сначала выведите количество конфет, которое выдано каждому ребенку,
# а затем количество конфет, что осталось в конфетном отсеке.


def get_num_of_candies(num_of_candies, num_of_children):
    equal_amount_candies_for_each_children = num_of_candies // num_of_children

    if equal_amount_candies_for_each_children == 0:
        return equal_amount_candies_for_each_children, num_of_candies

    return equal_amount_candies_for_each_children, num_of_candies % equal_amount_candies_for_each_children


if __name__ == '__main__':
    num_of_children = int(input())
    num_of_candies = int(input())

    equal_amount_candies_for_each_children, remain = get_num_of_candies(num_of_candies, num_of_children)
    print(f"{equal_amount_candies_for_each_children}\n{remain}")