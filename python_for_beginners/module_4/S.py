def format_string(value):
    f = "{}"
    if value > 18:
        f = "{:>2}"

    return f.format(value)


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{format_string(min(i, j, n - i + 1, n - j + 1))}', end=' ')
        print()