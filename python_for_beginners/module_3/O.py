# Зайка - 4
# Давайте вновь поиграем с детьми и поможем им найти заек.
# Формат ввода
# В первой строке записано натуральное число
# N — количество выделенных придорожных местностей. В каждой из
# N последующих строках — описание придорожной местности.
# Формат вывода
# Количество строк, в которых есть зайка.


def check_proposal_for_bunny(proposal: str):
    return "зайка" in proposal.split(sep=" ")


if __name__ == '__main__':
    num_of_proposal = int(input())
    count_proposal_with_bunny = 0

    for _ in range(num_of_proposal):
        if check_proposal_for_bunny(input()):
            count_proposal_with_bunny += 1

    print(count_proposal_with_bunny)
