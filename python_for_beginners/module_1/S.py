# Украшение чека
# Давайте приведём в порядок чек, который печатали ранее.
# Все строки должны быть длиной в 35 символов.
# Формат ввода
# Название товара;
# цена товара;
# вес товара;
# количество денег у пользователя.
# Формат вывода
# Красивый чек в формате:


def get_result_change(price, weight, money):
    result = price * weight
    change = money - result

    return result, change


def print_paycheck(title, price, weight, money, result, change):
    print("================Чек================")
    print("Товар:" + " " * (29 - len(title)) + f"{title}")
    print("Цена:" + " " * (19 - len(str(price)) - len(str(weight))) + f"{weight}" + "кг * " + f"{price}" + "руб/кг")
    print("Итого:" + " " * (26 - len(str(result))) + f"{result}" + "руб")
    print("Внесено:" + " " * (24 - len(str(money))) + f"{money}" + "руб")
    print("Сдача:" + " " * (26 - len(str(change))) + f"{change}" + "руб")
    print("===================================")


if __name__ == '__main__':
    title = input()
    price = int(input())
    weight = int(input())
    money = int(input())

    print_paycheck(title, price, weight, money, *get_result_change(price, weight, money))