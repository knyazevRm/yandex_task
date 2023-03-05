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


def is_closing_bracket(bracket, set_of_closing_bracket):
    return bracket in set_of_closing_bracket


def is_opening_bracket(bracket, set_of_opening_bracket):
    return bracket in set_of_opening_bracket


def get_index_of_bracket(bracket, set_of_bracket: list):
    return set_of_bracket.index(bracket)


def is_correct_bracket_sequence(brackets_seq, set_of_opening_bracket, set_of_closing_bracket):
    stack = Stack()

    for bracket in brackets_seq:
        if stack.is_empty():
            if is_closing_bracket(bracket, set_of_closing_bracket):
                return "no"

        if is_opening_bracket(bracket, set_of_opening_bracket):
            stack.push(bracket)
        else:
            if not stack.is_empty():
                if get_index_of_bracket(stack.back(), set_of_opening_bracket) == get_index_of_bracket(bracket, set_of_closing_bracket):
                    stack.pop()
                else:
                    return "no"
            else:
                return "no"

    return "yes" if stack.is_empty() else "no"


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    brackets_seq = reader.readline().strip()
    reader.close()

    set_of_closing_bracket = list("}])")
    set_of_opening_bracket = list("{[(")

    writer.write(is_correct_bracket_sequence(brackets_seq, set_of_opening_bracket, set_of_closing_bracket))

    writer.close()


if __name__ == '__main__':
    main()