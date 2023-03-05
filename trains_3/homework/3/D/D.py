def get_parent_pos(child_pos):
    return (child_pos - 1) // 2


def get_left_child_pos(parent_pos):
    return 2 * parent_pos + 1


def get_right_child_pos(parent_pos):
    return 2 * parent_pos + 2


class Heap:
    def __init__(self):
        self.__heap = []

    def size(self):
        return len(self.__heap)

    def push_heap(self, elem):
        self.__heap.append(elem)
        pos = self.size() - 1
        while pos > 0 and self.__heap[pos] > self.__heap[get_parent_pos(pos)]:
            self.__heap[pos], self.__heap[get_parent_pos(pos)] = self.__heap[get_parent_pos(pos)], self.__heap[pos]
            pos = get_parent_pos(pos)

    def pop_max_elem(self):
        result = self.__heap[0]
        self.__heap[0] = self.__heap[-1]
        pos = 0

        while get_right_child_pos(pos) < self.size():
            max_child_pos = get_left_child_pos(pos)
            if self.__heap[get_right_child_pos(pos)] > self.__heap[max_child_pos]:
                max_child_pos = get_right_child_pos(pos)
            if self.__heap[pos] < self.__heap[max_child_pos]:
                self.__heap[pos], self.__heap[max_child_pos] = self.__heap[max_child_pos], self.__heap[pos]
                pos = max_child_pos
            else:
                break

        self.__heap.pop()
        return result


def exec_command_return_result_running(param, heap, transition="\n"):
    command = param.split()

    if int(command[0]) == 1:
        return f"{heap.pop_max_elem()}{transition}"

    heap.push_heap(int(command[1]))

    return ""


def main():
    heap = Heap()

    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    count = int(reader.readline())

    while count > 1:
        writer.write(str(exec_command_return_result_running(reader.readline().strip(), heap)))
        count -= 1

    writer.write(str(exec_command_return_result_running(reader.readline().strip(), heap, transition="")))

    reader.close()
    writer.close()


if __name__ == '__main__':
    main()
