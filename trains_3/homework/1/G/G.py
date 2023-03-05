def str_time_to_sec(str_time: str):
    h, m, s = map(int, str_time.split(":"))

    return h * 60 * 60 + m * 60 + s


def transmission_time_in_both_directions(first, last):
    if first < last:
        return last - first

    return 24 * 60 * 60 - first + last


def offset(transmission_time):
    return transmission_time // 2 if transmission_time % 2 == 0 else transmission_time // 2 + 1


def sec_time_to_str(sec_time):
    h = (sec_time // (60 * 60)) % 24
    sec_time %= 60 * 60
    m = sec_time // 60
    sec_time %= 60
    s = sec_time % 60

    h = f"0{h}" if h < 10 else str(h)
    m = f"0{m}" if m < 10 else str(m)
    s = f"0{s}" if s < 10 else str(s)

    return f"{h}:{m}:{s}"


def main():
    reader = open('input.txt', 'r')
    A = str_time_to_sec(reader.readline())
    B = str_time_to_sec(reader.readline())
    C = str_time_to_sec(reader.readline())
    reader.close()

    writer = open('output.txt', 'w')
    writer.write(sec_time_to_str(offset(transmission_time_in_both_directions(A, C)) + B))
    writer.close()


if __name__ == '__main__':
    main()