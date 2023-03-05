def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    favourite_word = reader.readline().split()[0]
    dictionary_of_letter = {}
    N = len(favourite_word)

    for index in range(N):
        if favourite_word[index] in dictionary_of_letter.keys():
            dictionary_of_letter[favourite_word[index]] += (index + 1) * (N - index)
        else:
            dictionary_of_letter[favourite_word[index]] = (index + 1) * (N - index)

    reader.close()

    keys = sorted(dictionary_of_letter.keys())

    for i in range(len(keys) - 1):
        writer.write(f"{keys[i]}: {dictionary_of_letter[keys[i]]}\n")

    writer.write(f"{keys[len(keys) - 1]}: {dictionary_of_letter[keys[len(keys) - 1]]}")

    writer.close()


if __name__ == '__main__':
    main()