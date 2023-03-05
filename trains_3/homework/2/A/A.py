class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, elem):
        self.__stack.append(elem)

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if self.is_empty():
            return ""

        return self.__stack.pop()

    def clear(self):
        self.__stack.clear()

    def back(self):
        if self.is_empty():
            return ""

        return self.__stack[self.size() - 1]


def exec_command_return_result_running(command_str: str, stack) -> str:
    command = command_str.split()

    title_of_com = command[0]

    match title_of_com:
        case "push":
            stack.push(command[1])
            return "ok\n"
        case "pop":
            tmp_pop_elem = stack.pop()
            return "error\n" if str(tmp_pop_elem) == "" else str(tmp_pop_elem) + "\n"
        case "back":    
            tmp_back_elem = stack.back()
            return "error\n" if str(tmp_back_elem) == "" else str(tmp_back_elem) + "\n"
        case "clear":
            stack.clear()
            return "ok\n"
        case "size":
            return str(stack.size()) + "\n"


def main():
    stack = Stack()

    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    while True:
        tmp_com_str = reader.readline()
        if tmp_com_str == "exit\n":
            writer.write("bye")
            break
        else:
            writer.write(str(exec_command_return_result_running(tmp_com_str.strip(), stack)))

    reader.close()

    writer.close()


if __name__ == '__main__':
    main()