# import random


def get_counter_dict(message):
    counter_dict = dict()
    for char in message:
        if char in counter_dict:
            counter_dict[char] += 1
        else:
            if char != " ":
                counter_dict[char] = 1

    return counter_dict


# def quicksort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         q = random.choice(nums)
#     l_nums = [n for n in nums if n < q]
#
#     e_nums = [q] * nums.count(q)
#     b_nums = [n for n in nums if n > q]
#     return quicksort(l_nums) + e_nums + quicksort(b_nums)


def get_sorted_key_by_code_value(counter_of_key):
    return sorted(counter_of_key)


def max_value(counter):
    return max(counter.values())


def get_histogram(counter, sorted_keys):
    histogram = list()

    if len(counter) == 0:
        return histogram

    tmp_value = max_value(counter)
    while tmp_value > 0:
        tmp_row = ""
        for elem in sorted_keys:
            if counter[elem] == tmp_value:
                tmp_row += "#"
                counter[elem] -= 1
            else:
                tmp_row += " "
        tmp_value -= 1
        histogram.append(tmp_row)

    return histogram


def write_histogram(histogram, writer):
    for i in histogram:
        writer.write(i + "\n")


def main():
    reader = open('input.txt', 'r')

    message = ""
    for line in reader.readlines():
        message += line.strip()
    reader.close()

    counter = get_counter_dict(message)
    sorted_keys = get_sorted_key_by_code_value(list(counter.keys()))

    writer = open('output.txt', 'w')

    histogram = get_histogram(counter, sorted_keys)

    write_histogram(histogram, writer)
    writer.write("".join(sorted_keys))
    writer.close()


if __name__ == '__main__':
    main()