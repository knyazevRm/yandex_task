def filling_certain_area(cells, a, b, num_of_system):
    prev_cells = {0}
    count_of_work_system = 0
    for i in range(a - 1, b):
        if cells[i] not in prev_cells:
            prev_cells.add(cells[i])
            count_of_work_system -= 1

        cells[i] = num_of_system

    return count_of_work_system + 1


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    M = int(reader.readline())
    N = int(reader.readline())

    if N < 2:
        writer.write(str(N))
        return

    cells = [0 for _ in range(M)]

    count_of_work_system = 0

    for i in range(1, N + 1):
        a, b = map(int, reader.readline().split(" "))
        count_of_work_system += filling_certain_area(cells, a, b, i)

    reader.close()

    writer.write(str(count_of_work_system))
    writer.close()


if __name__ == '__main__':
    main()