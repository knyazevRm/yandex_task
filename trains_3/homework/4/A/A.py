def get_len_of_right_seq(N):
    dp = [2, 4, 7]
    for i in range(3, N):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

    return dp[N - 1]


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    len_of_seq = int(reader.readline())
    reader.close()

    writer.write(str(get_len_of_right_seq(len_of_seq)))

    writer.close()


if __name__ == '__main__':
    main()