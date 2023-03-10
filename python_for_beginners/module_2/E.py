# Яблоки
# У Пети было 7 яблок, а у Васи 6.
#
# Затем Петя отдал 3 яблока Васе, а у Толи взял 2 яблока.
#
# Вася попросил у Толи 5 яблок, но отдал Гене 2.
#
# Затем Дима дал Пете
# N
# N яблок, а Васе
# M
# M.
#
# Так у кого в итоге яблок больше — у Пети или Васи?
#
# Формат ввода
# В первой строке записано натуральное число
# N
# N.
# Во второй —
# M
# M.
#
# Формат вывода
# Имя ребёнка, у которого больше яблок.


# Пример 1

# Ввод
# 3
# 5

# Вывод
# Вася


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    num_for_petya = 7
    num_for_vasya = 6

    num_for_petya -= 3
    num_for_vasya += 3

    num_for_petya += 2

    num_for_vasya += 5
    num_for_vasya -= 2

    num_for_petya += N
    num_for_vasya += M

    if num_for_petya > num_for_vasya:
        print("Петя")
    else:
        print("Вася")