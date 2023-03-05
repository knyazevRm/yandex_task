def get_way_of_max_value(table, N, M, writer):
    NEGATIVE_NUM = -1
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    answer_coor = []
    answer_direction = []

    for i in range(2, N + 1):
        dp[i][0] = NEGATIVE_NUM

    for j in range(2, M + 1):
        dp[0][j] = NEGATIVE_NUM

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + table[i - 1][j - 1]

    writer.write(str(dp[-1][-1]))

    i, j = N, M
    while (i, j) != (1, 1):
        answer_coor.append((i, j))
        prev_dp = max(dp[i][j - 1], dp[i - 1][j])
        if dp[i][j - 1] == prev_dp:
            i, j = i, j - 1
            answer_direction.append("R")
        else:
            i, j = i - 1, j
            answer_direction.append("E")

    answer_direction = answer_direction[::-1]

    if len(answer_direction) > 0:
        writer.write("\n")
        writer.write(str(answer_direction[0]))
        for i in range(1, len(answer_direction)):
            writer.write(" " + str(answer_direction[i]))


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    N, M = map(int, reader.readline().split())

    table_of_penalties = []
    for _ in range(N):
        table_of_penalties.append(list(map(int, reader.readline().split())))
    reader.close()

    get_way_of_max_value(table_of_penalties, N, M, writer)
    writer.close()


if __name__ == '__main__':
    main()