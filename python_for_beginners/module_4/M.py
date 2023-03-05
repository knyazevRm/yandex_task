# Числовой прямоугольник 2.0

def create_matrix(width, length):
    return [[str(j * width + 1 + i) for j in range(length)] for i in range(width)]


def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(i.rjust(len(matrix[-1][-1])), end=" ")
        print()


if __name__ == '__main__':
    width, length = int(input()), int(input())
    print_matrix(create_matrix(width, length))