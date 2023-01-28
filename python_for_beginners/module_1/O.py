# В ожидании доставки
# Сегодня в N часов M минут хозяин магазина заказал доставку нового товара.
# Оператор сказал, что продукты доставят через T минут.
# Сколько будет времени на электронных часах, когда привезут долгожданные продукты?
# Формат ввода
# В первой строке записано натуральное число N (0≤N<24).
# Во второй строке записано натуральное число M (0≤M<60).
# В третьей строке записано натуральное число T (30≤T<10^9).
# Формат вывода
# Одна строка, представляющая циферблат электронных часов.


def get_delivery_time(N, M, T):
    total_num_minute_of_dial = (N * 60 + M + T) % (24 * 60)

    num_of_hours = total_num_minute_of_dial // 60
    num_of_minutes = total_num_minute_of_dial % (num_of_hours * 60) if num_of_hours != 0 else total_num_minute_of_dial

    return num_of_hours, num_of_minutes


def print_dial_time(hours, minutes):
    result = ""

    if hours < 10:
        result += "0"

    result += f"{hours}:"

    if minutes < 10:
        result += "0"

    result += f"{minutes}"

    return result


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    T = int(input())

    print(print_dial_time(*get_delivery_time(N, M, T)))