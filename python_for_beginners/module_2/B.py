# Кто быстрее?
# В главной велогонке года участвует более тысячи гонщиков. Им предстоит пройти трассу длинной 43872м. Самая сложная и ответственная задача — определение победителя.
#
# Нам известны средние скорости двух фаворитов — Пети и Васи. Помогите выяснить, кто из них пришёл к финишу первым.
#
# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
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

# Вывод
# Петя

if __name__ == '__main__':
    speed_of_petya = int(input())
    speed_of_vasya = int(input())

    if speed_of_petya > speed_of_vasya:
        print("Петя")
    else:
        print("Вася")