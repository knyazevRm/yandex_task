def check_two_interval(a, b, a_next, b_next):
    return ((a < a_next and a < b_next) and (b < a_next and b < b_next)) or ((a > a_next and a > b_next) and (b > a_next and b > b_next))


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    M = int(reader.readline())
    N = int(reader.readline())

    if N < 2:
        writer.write(str(N))
        writer.close()
        return

    count_of_work_system = N

    list_of_a_b = []

    for _ in range(N):
        a, b = map(int, reader.readline().split(" "))
        list_of_a_b.append((a, b))

    reader.close()

    for i in range(N - 1):
        for j in range(i + 1, N):
            if not check_two_interval(list_of_a_b[i][0], list_of_a_b[i][1], list_of_a_b[j][0], list_of_a_b[j][1]):
                count_of_work_system -= 1
                break

    writer.write(str(count_of_work_system))
    writer.close()


if __name__ == '__main__':
    main()