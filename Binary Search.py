
# def linear_search(numbers_list, number_to_find):
#     for index, element in enumerate(numbers_list):
#         if element == number_to_find:
#             return index
#     return False


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list)
    c_numbers_list = numbers_list.copy()
    mid_index = (left_index + right_index) // 2

    while mid_index:
        if number_to_find == numbers_list[mid_index - 1] or number_to_find == numbers_list[mid_index]:
            return str(c_numbers_list.index(number_to_find))
        if number_to_find < numbers_list[mid_index - 1] and number_to_find < numbers_list[mid_index]:
            numbers_list = numbers_list[:mid_index]
        elif number_to_find > numbers_list[mid_index - 1] and number_to_find > numbers_list[mid_index]:
            numbers_list = numbers_list[mid_index:]
        mid_index = mid_index // 2

    return False


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67, 88]
    number_to_find = 14

    index = binary_search(numbers_list, number_to_find)

    isnot = 'not ' if not index else ''
    index = index + ' ' if index else ''
    print(f'Number {isnot}found at index {index}using bi search.')















