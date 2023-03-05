def make_prefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(0, len(nums)):
        prefixsum[i + 1] = prefixsum[i] + nums[i]
    return prefixsum


def rsq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l]


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')
    N, M, K = map(int, reader.readline().split(" "))

    list_of_prefixsum_1D = list()

    for i in range(N):
        list_of_prefixsum_1D.append(make_prefixsum(list(map(int, reader.readline().split(" ")))))

    list_of_prefixsum_2D = [[0 for _ in range(M + 1)] for __ in range(N + 1)]

    for j in range(1, M + 1):
        for i in range(N):
            list_of_prefixsum_2D[i + 1][j] = list_of_prefixsum_2D[i][j] + list_of_prefixsum_1D[i][j]

    for query in range(K):
        x_1, y_1, x_2, y_2 = map(int, reader.readline().split(" "))
        curr_sum = list_of_prefixsum_2D[x_2][y_2] - list_of_prefixsum_2D[x_1 - 1][y_2] - list_of_prefixsum_2D[x_2][y_1 - 1] + list_of_prefixsum_2D[x_1 - 1][y_1 - 1]

        if query == K - 1:
            writer.write(str(curr_sum))
            reader.close()
        else:
            writer.write(str(curr_sum) + "\n")
    writer.close()


if __name__ == '__main__':
    main()