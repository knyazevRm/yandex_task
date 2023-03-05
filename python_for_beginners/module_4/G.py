# На старт! Внимание! Марш!
# По правилам велогонки,
# после квалификации каждый гонщик стартует с задержкой на секунду больше,
# чем у гонщика перед ним.
# Первый гонщик стартует на счёт 3.
# Напишите программу, которая сможет автоматизировать старт всех гонщиков,
# участвующих в велогонке.
#
# Формат ввода
# Вводится одно натуральное число — количество участников велогонки.
#
# Формат вывода
# Требуется вывести отсчёт.


def print_countdown(time, id):
    for i in range(time, 0, -1):
        print(f"До старта {i} секунд(ы)")

    print(f"Старт {id}!!!")


if __name__ == '__main__':
    time_to_start = 3
    number = int(input())
    for i in range(1, number + 1):
        print_countdown(time_to_start, i)
        time_to_start += 1