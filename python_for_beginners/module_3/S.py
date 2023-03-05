# Игра в «Угадайку»
# Давайте сымитируем игру «Угадайка» между двумя людьми.
# Для этого нужно написать программу, которая отгадывает загаданное целое число от 1 до 1000 включительно.
# Пользователь (или тестирующая система) загадывает число и не сообщает его вашей программе.
# Угадать число нужно не более, чем за 10 попыток.
#
# На каждую попытку пользователь отвечает одной из фраз:
#
# Больше;
# Меньше;
# Угадал!
# Данная задача проверяется интерактивно.
# Другими словами, пока вы не выведите своё число, система не предоставит вам данных.
import math


def middle_number_in_range(start, end):
    return math.ceil((start + end) / 2)


def settings(curr_num, start, end, state):
    return (curr_num, end) if state == "Больше" else (start, curr_num)


if __name__ == '__main__':
    start, end = 0, 1000
    curr_number = middle_number_in_range(0, 1000)
    print(curr_number)
    while (state := input()) != "Угадал!":
        start, end = settings(curr_number, start, end, state)
        curr_number = middle_number_in_range(start, end)
        print(curr_number)