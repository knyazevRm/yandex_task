class Queue:
    def __init__(self, queue):
        self.__queue = queue
        self.__head = 0
        self.__tail = len(self.__queue)

    def size(self):
        return self.__tail - self.__head

    def is_empty(self):
        return self.size() == 0

    def push(self, elem):
        if self.is_empty():
            self.__queue = []
            self.__head = 0
            self.__tail = 0

        self.__queue.append(elem)
        self.__tail += 1

    def front(self):
        return self.__queue[self.__head]

    def pop(self):
        first_elem = self.__queue[self.__head]
        self.__head += 1

        return first_elem

    def clear(self):
        self.__queue.clear()
        self.__head = 0
        self.__tail = 0


def compare_cards(l, r):
    if l > r:
        if r == 0 and l == 9:
            return False

        return True
    else:
        if l == 0 and r == 9:
            return True

        return False


def define_the_winner(first, second):
    count_of_step = 0
    while count_of_step <= 10 ** 6:
        if first.is_empty():
            return f"second {count_of_step}"

        if second.is_empty():
            return f"first {count_of_step}"

        card_of_first = first.pop()
        card_of_second = second.pop()

        if compare_cards(card_of_first, card_of_second):
            first.push(card_of_first)
            first.push(card_of_second)
        else:
            second.push(card_of_first)
            second.push(card_of_second)

        count_of_step += 1

    return "botva"


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    first, second = list(map(int, reader.readline().split())), list(map(int, reader.readline().split()))

    reader.close()

    writer.write(define_the_winner(Queue(first), Queue(second)))

    writer.close()


if __name__ == '__main__':
    main()
