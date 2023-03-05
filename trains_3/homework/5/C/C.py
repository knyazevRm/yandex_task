def get_count_step_for_horse(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    for i in range(2, N + 1):
        for j in range(2, M + 1):
            dp[i][j] = dp[i - 1][j - 2] + dp[i - 2][j - 1]

    return dp[-1][-1]


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    N, M = map(int, reader.readline().split())

    reader.close()

    writer.write(str(get_count_step_for_horse(N, M)))
    writer.close()


if __name__ == '__main__':
    main()