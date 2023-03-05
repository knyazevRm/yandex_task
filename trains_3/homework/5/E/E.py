def char_equals(s_1, s_2, n_1, n_2):
    return s_1[n_1] == s_2[n_2]


def get_answer(i, j, s_1, s_2, dp, writer):
    answer = []
    while i > 0 and j > 0:
        if s_1[i - 1] == s_2[j - 1]:
            answer.append(s_1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1

    return answer[::-1]


def get_max_sub_seq(N, s_1, M, s_2, writer):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if char_equals(s_1, s_2, i - 1, j - 1) else max(dp[i - 1][j], dp[i][j - 1])

    ans = get_answer(N, M, s_1, s_2, dp, writer)
    if len(ans) != 0:
        writer.write(str(ans[0]))
        for i in range(1, len(ans)):
            writer.write(" " + str(ans[i]))


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    N = int(reader.readline())
    s_1 = list(reader.readline().split())
    M = int(reader.readline())
    s_2 = list(reader.readline().split())

    reader.close()

    get_max_sub_seq(N, s_1, M, s_2, writer)
    writer.close()


if __name__ == '__main__':
    main()