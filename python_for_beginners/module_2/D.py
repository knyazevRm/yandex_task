# Список победителей
# Длинна трассы — 43872м, а зрители хотят узнать имя победителя.
#
# Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. Помогите подвести итоги гонки.
#
# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.
#
# Формат вывода
# Имена победителей в порядке занятых мест.

# Пример 1

# Ввод
# 10
# 5
# 7

# Вывод
# 1. Петя
# 2. Толя
# 3. Вася


if __name__ == '__main__':
    speed = list()

    for _ in range(3):
        speed.append(int(input()))

    name = ["Петя", "Вася", "Толя"]

    index = [i for i in range(3)]

    for i in range(len(speed)):
        for j in range(len(speed)):
            if speed[j] < speed[i]:
                tmp = speed[j]
                speed[j] = speed[i]
                speed[i] = tmp

                tmp_index = index[j]
                index[j] = index[i]
                index[i] = tmp_index

    for i in range(len(index)):
        print("{}. {}".format(i + 1, name[index[i]]))