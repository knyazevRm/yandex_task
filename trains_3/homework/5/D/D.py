def find_last_index_min_elem(last_day, INF):
    min_value = INF
    last_index = 0
    for i in range(len(last_day)):
        if last_day[i] <= min_value:
            min_value = last_day[i]
            last_index = i

    return last_index


def find_last_index_of_elem(array, elem):
    last_index = 0
    for i in range(1, len(array)):
        if array[i] == elem:
            last_index = i

    return last_index


def find_the_minimum_possible_total_cost(N, day_prices, writer):
    INF = 10 ** 6
    dp = [[0] * N for _ in range(N + 1)]

    for j in range(1, N):
        dp[0][j] = INF

    for i in range(1, N + 1):
        for j in range(N):
            if day_prices[i - 1] <= 100:
                if j + 1 == N:
                    dp[i][j] = dp[i - 1][j] + day_prices[i - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + day_prices[i - 1], dp[i - 1][j + 1])
            else:
                if j + 1 == N:
                    dp[i][j] = dp[i - 1][j - 1] + day_prices[i - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + day_prices[i - 1], dp[i - 1][j + 1])

    min_value = 0 if len(day_prices) == 0 else min(dp[-1])
    writer.write(str(min_value) + "\n")
    K_1 = find_last_index_min_elem(dp[-1], INF)
    K_2 = 0
    curr_j = K_1
    num_of_day_with_coupons = []
    if len(day_prices) > 1:
        for i in range(N, 0, -1):
            if dp[i][curr_j] == dp[i - 1][curr_j + 1] and dp[i][curr_j] < INF:
                num_of_day_with_coupons.append(i)
                curr_j += 1
                K_2 += 1
            else:
                min_value -= day_prices[i - 1]
                curr_j = find_last_index_of_elem(dp[i - 1], min_value)
    else:
        if len(day_prices) == 1:
            if day_prices[0] > 100:
                K_1 += 1

    num_of_day_with_coupons.reverse()
    writer.write(str(K_1) + " " + str(K_2))

    for i in range(len(num_of_day_with_coupons)):
        writer.write("\n" + str(num_of_day_with_coupons[i]))



def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    N = int(reader.readline())

    day_price = [int(reader.readline()) for _ in range(N)]

    reader.close()

    find_the_minimum_possible_total_cost(N, day_price, writer)
    writer.close()


if __name__ == '__main__':
    main()