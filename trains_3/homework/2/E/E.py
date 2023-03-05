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


def get_seq_of_relocations(length, seq_of_avg_cities_price):
    stack = Stack()
    seq_of_relocations = [-1 for _ in range(length)]
    for city in enumerate(seq_of_avg_cities_price):
        while not stack.is_empty() and stack.back()[1] > city[1]:
            seq_of_relocations[stack.pop()[0]] = city[0]

        stack.push(city)

    stack.clear()

    return seq_of_relocations


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    length = int(reader.readline())
    seq_of_avg_price_of_living_in_cities = list(map(int, reader.readline().split()))

    reader.close()

    result_seq = get_seq_of_relocations(length, seq_of_avg_price_of_living_in_cities)

    for i in range(length - 1):
        writer.write(str(result_seq[i]) + " ")

    writer.write(str(result_seq[length - 1]))
    writer.close()


if __name__ == '__main__':
    main()