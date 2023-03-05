# Редизайн таблицы умножения
# Согласитесь, что предыдущие таблицы умножения выглядят не очень красиво.
# Давайте зададим для всех столбцов одинаковую ширину, а значения в ячейках выровним по центру.
# И да, заказчик попросил ещё добавить в таблицу рамки между ячейками.
#
# Формат ввода
# В первой строке записан требуемый размер таблицы. Во второй строке — ширина столбцов.
#
# Формат вывода
# Таблица умножения заданного размера и вида.


def print_table_in_string_table(size, len):
    dash_ammount = (size * len) + len - 1
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f"{i * j:^{len}}", end="|" if j != size else "")
        if i < size:
            print("\n" + "-" * dash_ammount)


if __name__ == '__main__':
    size, len_of_cols = int(input()), int(input())
    print_table_in_string_table(size, len_of_cols)
