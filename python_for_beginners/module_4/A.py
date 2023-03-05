# Таблица умножения
# Местная фабрика канцелярских товаров заказала у вас программу,
# которая генерирует таблицы умножения.
# Давайте поддержим локального производителя!
#
# Формат ввода
# Вводится одно натуральное число — требуемый размер таблицы.
#
# Формат вывода
# Таблица умножения заданного размера.


def generate_multiplication_table(size):
    table = list()
    for i in range(1, size + 1):
        tmp_row = list()
        for j in range(1, size + 1):
            tmp_row.append(i * j)
        table.append(tmp_row)

    return table


def print_and_generate_table(size):
    for i in range(1, size + 1):
        print(*range(i, i * size + 1, i), sep="\t")


def print_table(table):
    for i in table:
        for j in i:
            print(j, end="\t")
        print()


if __name__ == '__main__':
    print_table(generate_multiplication_table(int(input())))
    #print_and_generate_table(9)