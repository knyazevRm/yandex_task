# Лучшая защита — шифрование
# Коля испугался, что Аня подсмотрит все его пароли в блокноте, и решил их зашифровать.
# Для этого он берёт изначальный пароль — трёхзначное число
# — и по нему строит новое число по следующим правилам:
#
# находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы);
# находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
# Эти две суммы, записанные друг за другом, в порядке не возрастания, формируют новое число.
# Помогите реализовать алгоритм шифрования.
#
# Формат ввода
# Одно трёхзначное число
#
# Формат вывода
# Результат шифрования

# Ввод
# 123

# Вывод
# 53


def encryption(num):
    str_of_num = str(num)
    num_of_hundreds = int(str_of_num[0])
    num_of_tens = int(str_of_num[1])
    junior_category = int(str_of_num[2])

    sum_of_senior_category = num_of_tens + num_of_hundreds
    sum_of_junior_category = num_of_tens + junior_category

    if sum_of_senior_category > sum_of_junior_category:
        return f"{sum_of_senior_category}{sum_of_junior_category}"

    return f"{sum_of_junior_category}{sum_of_senior_category}"


if __name__ == '__main__':
    number = int(input())

    print(encryption(number))