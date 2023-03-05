# А роза упала на лапу Азора 2.0
# Вспомним о палиндромах, которые в обоих направлениях читаются одинаково.
# Напишите программу, которая проверяет, является ли число палиндромом.
#
# Формат ввода
# Одно натуральное число.
#
# Формат вывода
# YES — если число является палиндромом, иначе — NO.


def check_polydrome(num):
    length = len(num)
    for i in range(length // 2):
        if num[i] != num[length - i - 1]:
            return False

    return True


if __name__ == '__main__':
    num = input()

    if check_polydrome(num):
        print("YES")
    else:
        print('NO')
