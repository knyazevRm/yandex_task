def get_count_stickers_that_less_given(sorted_set_of_stickers, length, target):
    mid = length // 2
    low = 0
    high = length - 1
    while sorted_set_of_stickers[mid] != target and low <= high:
        if target > sorted_set_of_stickers[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return low

    return mid


def main():
    reader = open('input.txt', 'r')

    num_of_diego_stickers = int(reader.readline())
    diego_stickers = set(map(int, reader.readline().split()))
    sorted_diego_stickers = sorted(diego_stickers)
    length_of_diego_stickers = len(diego_stickers)
    num_of_collectors = int(reader.readline())
    smallest_sticker_num_that_does_not_interest = list(map(int, reader.readline().split()))

    reader.close()

    writer = open('output.txt', 'w')

    for i in range(num_of_collectors):
        writer.write(str(get_count_stickers_that_less_given(sorted_diego_stickers, length_of_diego_stickers,
                                                            smallest_sticker_num_that_does_not_interest[i])))
        if i != num_of_collectors - 1:
            writer.write("\n")

    writer.close()


if __name__ == '__main__':
    main()
