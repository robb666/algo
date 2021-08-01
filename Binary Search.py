
# def linear_search(numbers_list, number_to_find):
#     for index, element in enumerate(numbers_list):
#         if element == number_to_find:
#             return index
#     return False


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    omo = []
    if right_index < left_index:
        return 'not found'

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        i = 1
        omo.append(mid_index)
        while mid_index + i <= len(numbers_list) - 1 \
                and (numbers_list[mid_index - i] == number_to_find or numbers_list[mid_index + i] == number_to_find):
            if numbers_list[mid_index - i] == number_to_find:
                omo.append(mid_index - i)
            if numbers_list[mid_index + i] == number_to_find:
                omo.append(mid_index + i)
            i += 1
        return sorted(omo)
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)



if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    numbers_list = [1,4,6,9,11,15,15,17,21,34,34,56,56]
    number_to_find = 56

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)

    print(f'Number found at index {index} using bi search.')








"""Binary Search 2"""
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return False




"""Binary Search 1"""
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


# numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
# number_to_find = 19
#
# index = binary_search(numbers_list, number_to_find)
# print(index)




