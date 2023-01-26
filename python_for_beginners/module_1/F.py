if __name__ == '__main__':
    title = input()
    price = int(input())
    weight = int(input())
    money = int(input())

    print("Чек")
    print(f"{title} - {weight}кг - {price}руб/кг")
    print(f"Итого: {price * weight}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {money - price * weight}руб")