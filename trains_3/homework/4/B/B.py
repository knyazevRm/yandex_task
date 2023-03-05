def get_num_of_ways(N, k):
    dp = [0] * N
    dp[0] = 1

    for i in range(1, N):
        curr_step = 1
        while i - curr_step >= 0 and curr_step <= k:
            dp[i] += dp[i - curr_step]
            curr_step += 1

    return dp[N - 1]


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    len_of_seq, max_step = map(int, reader.readline().split())
    reader.close()

    writer.write(str(get_num_of_ways(len_of_seq, max_step)))

    writer.close()


if __name__ == '__main__':
    main()