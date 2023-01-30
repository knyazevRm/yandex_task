# Излишняя автоматизация 2.0
# А что будет, если вновь, как в первой главе,
# объединить два принципа — повторение и автоматизацию?
#
# Формат ввода
# В первой строке записана весьма полезная информация. Во второй натуральное число
# N — количество раз, которое её нужно повторить, чтобы она закрепилась.
#
# Формат вывода
# N раз повторенная весьма полезная информация.


def print_str(proposal: str, num_of_str: int):
    for _ in range(num_of_str):
        print(proposal)


if __name__ == '__main__':
    proposal = input()
    num = int(input())

    print_str(proposal, num)