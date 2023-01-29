# Зайка — 3
# В задачнике ко второй лекции мы помогали детям искать зайца.
# На этот раз мы будем искать и считать сразу нескольких зайчат.
#
# Формат ввода
# Вводятся строки, описывающие придорожную местность.
# В конце поездки вводится «Приехали!»
#
# Формат вывода
# Количество строк, в которых есть зайка.


def check_buddy(proposal: str):
    for word in proposal.split(sep=" "):
        if word == "зайка":
            return True

    return False


def get_count_of_proposal():
    count = 0
    while (proposal := input()) != "Приехали!":
        if check_buddy(proposal):
            count += 1

    return count


if __name__ == '__main__':
    print(get_count_of_proposal())