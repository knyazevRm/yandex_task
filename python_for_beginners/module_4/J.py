# Мы делили апельсин
# Аня, Боря и Вова решили съесть апельсин.
# Подскажите ребятам, как им его разделить.
# Напишите программу, которая выводит все возможные способы разделки апельсина.
#
# Формат ввода
# В единственной строке записано количество долек апельсина.
#
# Формат вывода
# Таблица вариантов разделения апельсина.
#
# Примечания
# Каждому ребёнку должна достаться хотя бы одна долька апельсина.
# Ни одной дольки не должно остаться.
# Выводить варианты в порядке увеличения количества долек у Ани, затем Бори и затем уже Вовы.


import itertools


def all_combination(num_of_orange):
    init = [i for i in range(1, num_of_orange - 1)]
    result = list()

    for i in itertools.product(init, repeat=3):
        if sum([elem for elem in i]) == num_of_orange:
            result.append(i)

    return result


if __name__ == '__main__':
    number_of_orange = int(input())
    print("А Б В")
    for i in all_combination(number_of_orange):
        print(*i, sep=" ")
