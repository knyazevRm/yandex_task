import math


def diff_of_row(petya, vasya):
    if vasya > petya:
        return vasya - petya - 1

    return petya - vasya - 1


def find_close_place(num_of_students, num_of_variants, petya_row, pos):
    number_of_petya_place = 2 * (petya_row - 1) + pos
    num_vasya_place_at_the_front = number_of_petya_place - 1 - num_of_variants
    num_vasya_place_from_behind = number_of_petya_place + num_of_variants

    if num_vasya_place_at_the_front < 0 and num_vasya_place_from_behind > num_of_students:
        return str(-1)

    vasya_row = -1
    vasya_pos = -1

    if num_vasya_place_at_the_front >= 0:
        vasya_row = petya_row - (math.ceil((num_of_variants - 1) / 2) if pos == 2 else math.ceil(num_of_variants / 2))
        vasya_pos = 2 if (pos + num_of_variants) % 2 == 0 else 1

    if num_vasya_place_from_behind <= num_of_students:
        tmp_row = math.ceil(num_of_variants / 2) if pos == 2 else math.ceil((num_of_variants - 1) / 2)
        if vasya_row == -1 or diff_of_row(petya_row, vasya_row) >= tmp_row - 1:
            vasya_row = tmp_row + petya_row
            vasya_pos = 2 if (pos + num_of_variants) % 2 == 0 else 1

    return str(f"{vasya_row} {vasya_pos}")


def main():
    reader = open('input.txt', 'r')
    num_of_students = int(reader.readline())
    num_of_variants = int(reader.readline())
    petya_row = int(reader.readline())
    position = int(reader.readline())

    reader.close()

    writer = open('output.txt', 'w')
    writer.write(find_close_place(num_of_students, num_of_variants, petya_row, position))
    writer.close()


if __name__ == '__main__':
    main()