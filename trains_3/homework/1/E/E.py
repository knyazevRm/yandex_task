def main():
    reader = open('input.txt', 'r')
    writer = open('output.txt', 'w')

    counter_dict_of_alphabet = {}

    num_of_letter = int(reader.readline())

    result = 0

    for char in range(num_of_letter):
        counter_dict_of_alphabet[char] = int(reader.readline())

        if char - 1 in counter_dict_of_alphabet.keys():
            result += counter_dict_of_alphabet[char - 1] if counter_dict_of_alphabet[char] >= counter_dict_of_alphabet[char - 1] else counter_dict_of_alphabet[char]

    reader.close()

    writer.write(str(result))
    writer.close()


if __name__ == '__main__':
    main()