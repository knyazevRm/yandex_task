# Числовая змейка
# Увы, обыкновенные прямоугольники детям быстро наскучили.
# Теперь воспитательнице требуется новая программа.
# Напишите программу, которая строит числовую змейку требуемого размера.


def create_matrix(width, length):
    return [create_row(i, length) if i % 2 == 0 else get_reverse_row(create_row(i, length)) for i in range(width)]


def create_row(i, length):
    return [str(i * length + j + 1) for j in range(length)]


def get_reverse_row(row):
    row.reverse()
    return row


def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(i.rjust(len(matrix[-1][-1])), end=" ")
        print()


if __name__ == '__main__':
    width, length = int(input()), int(input())
    print_matrix(create_matrix(width, length))