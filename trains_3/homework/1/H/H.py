def main():
    reader = open('input.txt', 'r')
    num_of_points = int(reader.readline())
    min_x, min_y = 10 ** 9, 10 ** 9
    max_x, max_y = -10 ** 9, -10 ** 9

    for _ in range(num_of_points):
        x, y = map(int, reader.readline().split(" "))

        if min_x > x:
            min_x = x

        if max_x < x:
            max_x = x

        if min_y > y:
            min_y = y

        if max_y < y:
            max_y = y

    reader.close()

    writer = open('output.txt', 'w')
    writer.write(f"{min_x} {min_y} {max_x} {max_y}")
    writer.close()


if __name__ == '__main__':
    main()