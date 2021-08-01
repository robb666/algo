
# def linear_search(numbers_list, number_to_find):
#     for index, element in enumerate(numbers_list):
#         if element == number_to_find:
#             return index
#     return False


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1

    mid_index = 1 + (left_index + right_index) // 2
    while mid_index > 0:
        if number_to_find == numbers_list[mid_index] or number_to_find == numbers_list[mid_index - 1]:
            return True
        if number_to_find < numbers_list[mid_index] and number_to_find < numbers_list[mid_index - 1]:
            numbers_list = numbers_list[:mid_index]
        elif number_to_find > numbers_list[mid_index] and number_to_find > numbers_list[mid_index - 1]:
            numbers_list = numbers_list[mid_index:]
        mid_index = mid_index // 2

    return False


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67, 88]
    number_to_find = 88

    isin = binary_search(numbers_list, number_to_find)
    print(isin)
    # print(f'Number found')  # at index {index} using bi search.')















