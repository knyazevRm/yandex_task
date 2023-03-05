def get_min_weight(table, N, M):
    INF = 10 ** 4
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(2, N + 1):
        dp[i][0] = INF
    for j in range(2, M + 1):
        dp[0][j] = INF

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + table[i - 1][j - 1]

    return dp[-1][-1]


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    N, M = map(int, reader.readline().split())

    table_of_penalties = []
    for _ in range(N):
        table_of_penalties.append(list(map(int, reader.readline().split())))
    reader.close()

    writer.write(str(get_min_weight(table_of_penalties, N, M)))
    writer.close()


if __name__ == '__main__':
    main()