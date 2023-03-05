# Числовая змейка 2.0
# Воспитательнице вновь нужна программа,
# которая будет генерировать змейку из чисел.
# Напишите программу, которая строит числовую змейку требуемого размера.


def create_matrix(width, length):
    return [[0] * width for _ in range(length)]


def print_matrix(matrix, width, length):
    dd = len(str(width * length))
    for row in matrix:
        for i in row:
            print(f'{i:>{dd}}', end=' ')
        print()


def fill_data(matrix, width, length):
    counter = 1
    for j in range(width):
        if j % 2 == 0:
            for i in range(length):
                matrix[i][j] = str(counter)
                counter += 1
        else:
            for i in range(length - 1, -1, -1):
                matrix[i][j] = str(counter)
                counter += 1


if __name__ == '__main__':
    length, width = int(input()), int(input())
    matrix = create_matrix(width, length)
    fill_data(matrix, width, length)
    print_matrix(matrix, width, length)