# Суммарная сумма
# Найти сумму цифр числа не так сложно, но что, если чисел несколько?
# Напишите программу для выполнения этого действия.
#
# Формат ввода
# В первой строке указано число
# N Во всех последующих
# N строках написано по одному числу.
#
# Формат вывода
# Требуется вывести общую сумму цифр всех введённых чисел (кроме N).


def suma_of_digit_of_number(number):
    suma = 0
    while number > 0:
        suma += number % 10
        number //= 10

    return suma


if __name__ == '__main__':
    result_suma = 0
    for i in range(int(input())):
        result_suma += suma_of_digit_of_number(int(input()))

    print(result_suma)