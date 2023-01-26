# Зайка — 1
# В долгой дороге дети могут капризничать, поэтому родители их развлекают с помощью игр.
# Одна из них — поиск различных зверушек в придорожной растительности.
#
# Давайте немного поиграем и выясним, не спрятался ли зайка во введённом предложении.
#
# Формат ввода
# Строка описывающая придорожную местность.
#
# Формат вывода
# YES — если в этой местности есть зайка, иначе — NO.


def find_bunny(string_of_terrain):
    for i in roadside_terrain.split(sep=" "):
        if i == "зайка":
            return True

    return False


if __name__ == '__main__':
    roadside_terrain = str(input())

    if find_bunny(roadside_terrain):
        print("YES")
    else:
        print("NO")