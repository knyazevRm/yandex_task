def get_min_time(A, B, C, num_of_human):
    dp = [0] * num_of_human
    dp[0] = A[0]

    if num_of_human > 1:
        dp[1] = min(A[0] + A[1], B[0])

    if num_of_human > 2:
        dp[2] = min(A[0] + A[1] + A[2], B[0] + A[2], A[0] + B[1], C[0])

    for i in range(3, num_of_human):
        dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i - 1], dp[i - 3] + C[i - 2])

    return dp[-1]


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    num_of_human = int(reader.readline())
    A = [0] * num_of_human
    B = [0] * num_of_human
    C = [0] * num_of_human

    for i in range(num_of_human):
        A[i], B[i], C[i] = map(int, reader.readline().split())
    reader.close()

    writer.write(str(get_min_time(A, B, C, num_of_human)))
    writer.close()


if __name__ == '__main__':
    main()