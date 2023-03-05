# Математическая выгода
# Математик Виталий Евгеньевич задумался над вопросом выгоды систем счисления.
# Он решил, что выгодной системой счисления будет являться та,
# в которой число имеет наибольшую сумму цифр.
# Напишите программу,
# которая по введённому числу определяет основание системы счисления с максимальной выгодой.


def get_digit_of_num_in_new_system(num, system):
    sum = 0
    while num != 0:
        sum += num % system
        num //= system

    return sum


if __name__ == '__main__':
    num = int(input())
    list_of_sum = []
    for i in range(2, 11):
        list_of_sum.append(get_digit_of_num_in_new_system(num, i))

    print(list_of_sum.index(max(list_of_sum)) + 2)