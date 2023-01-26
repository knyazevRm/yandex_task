# Кто быстрее на этот раз?
# Вновь велогонщики собрались узнать, кто из них быстрее. Им предстоит пройти трассу длиной 43872м, и нам нужно вновь определить победителя.
#
# На этот раз нам известны средние скорости трёх фаворитов — Пети, Васи и Толи. Кто из них пришёл к финишу первым?
#
# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.
#
# Формат вывода
# Имя победителя гонки.
#
# Примечание
# Гарантируется, что победителем стал только один.

# Пример 1

# Ввод
# 10
# 5
# 7

# Вывод
# Петя


if __name__ == '__main__':
    speed_of_petya = int(input())
    speed_of_vasya = int(input())
    speed_of_tolya = int(input())

    if speed_of_petya > speed_of_vasya:
        if speed_of_petya > speed_of_tolya:
            print("Петя")
        else:
            if speed_of_tolya > speed_of_vasya:
                print("Толя")
            else:
                print("Вася")
    else:
        if speed_of_vasya > speed_of_tolya:
            print("Вася")
        else:
            if speed_of_petya > speed_of_tolya:
                print("Петя")
            else:
                print("Толя")