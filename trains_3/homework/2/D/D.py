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


def sorting_of_wagons(seq_of_wagons, length):
    stack = Stack()
    curr_allowed_wagon_num = 1
    for num_of_wagon in seq_of_wagons:
        if num_of_wagon == curr_allowed_wagon_num:
            curr_allowed_wagon_num += 1
            if not stack.is_empty():
                while curr_allowed_wagon_num == stack.back():
                    curr_allowed_wagon_num += 1
                    stack.pop()
        else:
            stack.push(num_of_wagon)

    if curr_allowed_wagon_num == length:
        return "YES"

    while curr_allowed_wagon_num == stack.back():
        curr_allowed_wagon_num += 1
        stack.pop()

    return "YES" if stack.is_empty() else "NO"


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    length = int(reader.readline())
    seq_of_wagons = list(map(int, reader.readline().split()))

    reader.close()

    writer.write(sorting_of_wagons(seq_of_wagons, length))
    writer.close()


if __name__ == '__main__':
    main()
