def max_length_of_same_char(S):
    count, max_count = 0, 0
    for i in range(len(S)):
        if i == 0 or S[i - 1] == S[i]:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 1

    return max_count


def get_counter_dictionary(init_line):
    counter_dict = {}
    for char in init_line:
        if char in counter_dict.keys():
            counter_dict[char] += 1
        else:
            counter_dict[char] = 1

    return dict(sorted(counter_dict.items(), key=lambda item:item[1], reverse=True))


def find_beautiful_line_alphabet(init_line, k):
    max_result = 0
    alphabet = [chr(i) for i in range(ord('a'), ord('a') + 26)]

    for letter in alphabet:
        t = k
        count = 0
        left, right = 0, 0
        for i in range(0, len(init_line)):
            if letter == init_line[i]:
                right += 1
                count += 1
                max_result = max(max_result, count)
            else:
                if t > 0:
                    t -= 1
                    right += 1
                    count += 1
                    max_result = max(max_result, count)
                else:
                    while left < right:
                        if init_line[left] == letter:
                            left += 1
                            count -= 1
                        else:
                            left += 1
                            right += 1
                            break

    return max_result


def find_beautiful_line_use_dict(init_line, k):
    max_result = 0
    counter_dict = get_counter_dictionary(init_line)

    for letter in counter_dict.keys():
        t = k
        count = 0
        left, right = 0, 0
        for char in init_line:
            if letter == char:
                right += 1
                count += 1
                if max_result < count:
                    max_result = count
            else:
                if t > 0:
                    t -= 1
                    right += 1
                    count += 1
                    if max_result < count:
                        max_result = count
                else:
                    while left < right:
                        if init_line[left] == letter:
                            left += 1
                            count -= 1
                        else:
                            left += 1
                            right += 1
                            break

    return max_result


def main():
    reader = open('input.txt', 'r')

    k = int(reader.readline())
    S = reader.readline()

    reader.close()

    writer = open('output.txt', 'w')
    writer.write(str(find_beautiful_line_use_dict(S, k)))
    writer.close()


if __name__ == '__main__':
    main()
