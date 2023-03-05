def get_min_num_of_operation(target, writer):
    dp = [0] * (target + 1)
    arr_of_num = [1]

    for i in range(2, target + 1):
        prev_count_of_step = dp[i - 1]
        if i % 2 == 0:
            prev_count_of_step = min(prev_count_of_step, dp[i // 2])
        if i % 3 == 0:
            prev_count_of_step = min(prev_count_of_step, dp[i // 3])
        dp[i] = prev_count_of_step + 1

    writer.write(f"{dp[-1]}\n")
    writer.write(f"{arr_of_num[-1]}")

    i = target
    while i > 1:
        if dp[i] == dp[i - 1] + 1:
            arr_of_num.insert(1, i)
            i -= 1
            continue
        if i % 2 == 0 and dp[i] == dp[i // 2] + 1:
            arr_of_num.insert(1, i)
            i //= 2
            continue
        if i % 3 == 0 and dp[i] == dp[i // 3] + 1:
            arr_of_num.insert(1, i)
            i //= 3

    for i in range(1, len(arr_of_num)):
        writer.write(f" {arr_of_num[i]}")


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    target = int(reader.readline())
    reader.close()

    get_min_num_of_operation(target, writer)

    writer.close()


if __name__ == '__main__':
    main()