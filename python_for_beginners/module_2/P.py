# Легенды велогонок возвращаются: кто быстрее?
# В новом сезоне за первенство в велогонках вновь борются лучшие из лучших.
# Протяжённость заключительной трассы — 43872м, и все хотят знать, кто получит золотую медаль.
#
# Нам известны средние скорости трёх претендентов на победу – Пети, Васи и Толи. Кто из них победит?
#
# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.
#
# Формат вывода
# Красивый пьедестал (ширина ступеней 8 символов).


def create_list_of_winners(speed):
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

    return index


def print_pedestal(list_of_winners):
    name = ["Петя", "Вася", "Толя"]

    print(f"          {name[list_of_winners[0]]}          ")
    print(f"  {name[list_of_winners[1]]}                  ")
    print(f"                  {name[list_of_winners[2]]}  ")
    print("   II      I      III   ")


if __name__ == '__main__':
    speed = list()

    for _ in range(3):
        speed.append(int(input()))

    print_pedestal(create_list_of_winners(speed))