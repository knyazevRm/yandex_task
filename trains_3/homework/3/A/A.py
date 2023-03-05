class Queue:
    def __init__(self):
        self.__queue = []
        self.__head = 0
        self.__tail = 0

    def size(self):
        return self.__tail - self.__head

    def is_empty(self):
        return self.size() == 0

    def push(self, elem):
        self.__queue.append(elem)
        self.__tail += 1

    def front(self):
        if self.is_empty():
            return "error"

        return self.__queue[self.__head]

    def pop(self):
        if self.is_empty():
            return "error"

        first_elem = self.__queue[self.__head]
        self.__head += 1

        return first_elem

    def clear(self):
        self.__queue.clear()
        self.__head = 0
        self.__tail = 0


def exec_command_return_result_running(command_str, queue):
    command = command_str.split()

    title_of_com = command[0]

    match title_of_com:
        case "push":
            queue.push(command[1])
            return "ok\n"
        case "pop":
            return f"{queue.pop()}\n"
        case "front":
            return f"{queue.front()}\n"
        case "clear":
            queue.clear()
            return "ok\n"
        case "size":
            return f"{queue.size()}\n"


def main():
    queue = Queue()

    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    while True:
        tmp_com_str = reader.readline()
        if tmp_com_str == "exit\n":
            writer.write("bye")
            break
        else:
            writer.write(str(exec_command_return_result_running(tmp_com_str.strip(), queue)))

    reader.close()

    writer.close()


if __name__ == '__main__':
    main()
