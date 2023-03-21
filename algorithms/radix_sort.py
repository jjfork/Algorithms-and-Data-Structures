from helpers.timeit import timeit


@timeit
def radix_sort(input_array: list):
    max_len = len(str(max(input_array)))
    for position in range(max_len):
        digit_counter = dict.fromkeys(range(10))
        for key in digit_counter:
            digit_counter[key] = list()

        for number in input_array:
            number_after_cut = int(number / 10 ** position)
            digit_in_pos = number_after_cut % 10
            digit_counter[digit_in_pos].append(number)

        temp_num = list()

        for digit in range(10):
            temp_num += digit_counter[digit]

        input_array = temp_num

    return input_array



