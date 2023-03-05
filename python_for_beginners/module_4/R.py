if __name__ == '__main__':
    count = int(input())
    index = 1
    row = 1
    while index <= count:
        print(' ' * (count - row), end='')
        for col in range(row):
            print(f"{index}", end=' ')
            index += 1
            if index > count:
                break
        row += 1
        print()