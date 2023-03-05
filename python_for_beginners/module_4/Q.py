def num_is_palindrom(num):
    length = len(num)
    for i in range(length // 2):
        if num[i] != num[length - i - 1]:
            return False

    return True


if __name__ == '__main__':
    count = 0
    n = int(input())

    for _ in range(n):
        if num_is_palindrom(input()):
            count += 1

    print(count)