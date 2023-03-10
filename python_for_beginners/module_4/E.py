# Зайка — 5
# В долгой дороге дети вновь заскучали,
# и родителям приходится их развлекать поиском зверушек за окном. Давайте вместе с ними найдём заек.
#
# Формат ввода
# В первой строке указано натуральное число
# N — количество выделенных придорожных местностей.
# В последующих строках записаны слова характеризующие выделенную местность.
# Информация о каждой местности завершается словом «ВСЁ».
#
# Формат вывода
# Количество местностей, в которых есть зайка.


def check_str(curr_str):
    return curr_str == "зайка"


if __name__ == '__main__':
    result = 0
    flag = True
    count = int(input())
    while count > 0:
        string = input()
        if string == "ВСЁ":
            count -= 1
            flag = True
        if flag:
            if check_str(string):
                result += 1
                flag = False

    print(result)