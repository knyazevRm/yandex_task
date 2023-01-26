# А роза упала на лапу Азора
# Существуют такое интересное понятие как палиндром
# — число, слово, предложение и так далее, которое и слева-направо,
# и справа-налево читается одинаково.
#
# Напишите программу, которая проверяет, является ли число палиндромом.
#
# Формат ввода
# Одно четырёхзначное число
#
# Формат вывода
# YES если число является палиндромом, иначе — NO.

# Пример 1

# Ввод
# 1234

# Вывод
# NO


def check_palindrome(num):
    obj: str = str(num)
    len_of_obj = len(obj)

    for i in range(len_of_obj // 2):
        if obj[i] != obj[len_of_obj - i - 1]:
            return False

    return True


if __name__ == '__main__':
    num = int(input())

    if check_palindrome(num):
        print("YES")
    else:
        print("NO")