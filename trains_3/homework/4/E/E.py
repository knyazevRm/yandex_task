def get_min_length_of_lines(length, seq):
    seq.sort()
    dp = [0] * (length + 1)
    dp[2] = seq[1] - seq[0]
    if length > 2:
        dp[3] = seq[2] - seq[0]
    for i in range(4, length + 1):
        dp[i] = min(dp[i - 2], dp[i - 1]) + seq[i - 1] - seq[i - 2]

    return dp[-1]


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    length_of_seq = int(reader.readline())

    seq = list(map(int, reader.readline().split()))
    reader.close()

    writer.write(str(get_min_length_of_lines(length_of_seq, seq)))
    writer.close()


if __name__ == '__main__':
    main()