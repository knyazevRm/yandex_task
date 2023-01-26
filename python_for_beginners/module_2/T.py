# Зайка — 2
# По пути домой родители вновь решили сыграть с детьми в поиск зверушек.
#
# Формат ввода
# Три строки описывающих придорожную местность.
#
# Формат вывода
# Строка в которой есть зайка, а затем её длина.
# Если таких строк несколько, выбрать ту, что меньше всех лексикографически.


def check_str(string: str):
    return "зайка" in string.split(sep=" ")


def main(*strings):
    result = list()

    for tmp_str in strings:
        if check_str(tmp_str):
            result.append(tmp_str)

    min_str = min(result)

    return f"{min_str} {len(min_str)}"


if __name__ == '__main__':
    first_str = input()
    second_str = input()
    third_str = input()

    print(main(first_str, second_str, third_str))