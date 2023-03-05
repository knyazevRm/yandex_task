def get_left_child_pos(parent_pos):
    return 2 * parent_pos + 1


def get_right_child_pos(parent_pos):
    return 2 * parent_pos + 2


def heapify(arr, N, i):
    largest = i
    l = get_left_child_pos(i)
    r = get_right_child_pos(i)

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, N, largest)


def heapsort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    result_arr = f"{arr[0]}"
    for i in range(1, N):
        result_arr += f" {arr[i]}"

    return result_arr


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    count = int(reader.readline())

    writer.write(heapsort(list(map(int, reader.readline().split()))))
    reader.close()
    writer.close()


if __name__ == '__main__':
    main()