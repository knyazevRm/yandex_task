class Node:
    def __init__(self, value=None, front=None, back=None):
        self.__value = value
        self.__prev = front
        self.__next = back

    @property
    def value(self):
        return self.__value

    @property
    def prev(self):
        return self.__prev

    @property
    def next(self):
        return self.__next

    @value.setter
    def value(self, elem):
        self.__value = elem

    @prev.setter
    def prev(self, node):
        self.__prev = node

    @next.setter
    def next(self, node):
        self.__next = node


class Deque:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def insert_in_emptylist(self, data):
        node = Node(data)
        self.__head = node
        self.__tail = node

    def push_front(self, data):
        if self.__head is None:
            self.insert_in_emptylist(data)
        else:
            node = Node(data, None, self.__head)
            self.__head.prev = node
            self.__head = node

        self.__size += 1

    def push_back(self, data):
        if self.__tail is None:
            self.insert_in_emptylist(data)
        else:
            node = Node(data, self.__tail, None)
            self.__tail.next = node
            self.__tail = node

        self.__size += 1

    def back(self):
        if self.is_empty():
            return "error"
        else:
            return self.__tail.value

    def front(self):
        if self.is_empty():
            return "error"
        else:
            return self.__head.value

    def remove_begin(self):
        result = self.__head.value

        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None

        else:
            self.__head = self.__head.next
            self.__head.prev = None

        self.__size -= 1

        return result

    def remove_back(self):
        result = self.__tail.value

        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None

        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None

        self.__size -= 1

        return result

    def pop_back(self):
        if self.is_empty():
            return "error"
        else:
            return self.remove_back()

    def pop_front(self):
        if self.is_empty():
            return "error"
        else:
            return self.remove_begin()


def exec_command_return_result_running(command_str, deque):
    command = command_str.split()

    title_of_com = command[0]

    match title_of_com:
        case "push_back":
            deque.push_back(command[1])
            return "ok\n"
        case "push_front":
            deque.push_front(command[1])
            return "ok\n"
        case "pop_back":
            return f"{deque.pop_back()}\n"
        case "pop_front":
            return f"{deque.pop_front()}\n"
        case "back":
            return f"{deque.back()}\n"
        case "front":
            return f"{deque.front()}\n"
        case "clear":
            deque.clear()
            return "ok\n"
        case "size":
            return f"{deque.size()}\n"


def main():
    deque = Deque()

    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    while True:
        tmp_com_str = reader.readline()
        if tmp_com_str == "exit\n":
            writer.write("bye")
            break
        else:
            writer.write(str(exec_command_return_result_running(tmp_com_str.strip(), deque)))

    reader.close()

    writer.close()


if __name__ == '__main__':
    main()