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


def result_of_expression(postfix_str, set_of_operation):
    result: str = ""
    stack = Stack()
    for char in postfix_str:
        if char not in set_of_operation:
            if char == ")":
                while stack.back() != "(":
                    result += stack.pop()
            else:
                stack.push(char)
        else:
            prev_operand = stack.pop()
            prev_prev_operand = stack.pop()
            stack.push(eval(f"{prev_prev_operand}{char}{prev_operand}"))

    return str(stack.pop())


def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    set_of_operation = set("+-*")
    expression = list(map(str, reader.readline().split()))

    reader.close()

    writer.write(result_of_expression(expression, set_of_operation))
    writer.close()


if __name__ == '__main__':
    main()