import timeit
import random


def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return False


def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == num:
            return mid
        elif guess > num:
            high = mid - 1
        else:
            low = mid + 1
    return False


def linear_performance():
    """Performace measurment with Monte Carlo simulation"""
    run_setup = """
import random
from __main__ import linear_search
"""

    run_code = """
test_list = list(range(1,random.randint(2,100)))
test_number = random.randint(2, 100)
linear_search(test_list,test_number)
"""

    performance = timeit.repeat(setup=run_setup,
                                    stmt=run_code,
                                    repeat=3,
                                    number=100_000)
    print(f'linear search performance = {round(min(performance), 2)}')




def binary_search_performance():
    """Performace measurment with Monte Carlo simulation"""
    run_setup = """
import random
from __main__ import binary_search
"""

    run_code = """
test_list = list(range(1,random.randint(2,100)))
test_number = random.randint(2, 100)
binary_search(test_list,test_number)
"""

    performance = timeit.repeat(setup=run_setup,
                                    stmt=run_code,
                                    repeat=3,
                                    number=100_000)
    print(f'binary search performance = {round(min(performance), 2)}')


linear_performance()
binary_search_performance()









"""Binary Search 5"""
def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == num:
            return mid
        elif guess > num:
            high = mid - 1
        else:
            low = mid + 1
    return False


# if __name__ == '__main__':
#     numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
#     print(binary_search(numbers_list, 24))
#
#     numbers_list = list(range(400002))
#     # print(numbers_list)
#     print(binary_search(numbers_list, 400001))








"""Binary Search 4 """
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find: # this means number is in right hand side of the list
            left_index = mid_index + 1
        else: # number to find is on left hand side of the list
            right_index = mid_index - 1

    return -1


def find_all_occurences(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]

    # find indices on left hand site
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i -= 1

    # find indices on the right hand site
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i += 1

    return sorted(indices)


# if __name__ == '__main__':
#     # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
#     numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56,56]
#     number_to_find = 15
#
#     index = find_all_occurences(numbers_list, number_to_find)
#
#     print(f'Number found at index {index} using bi search.')















"""Binary Search 3"""
def find_all_occurences(numbers_list, number_to_find, left_index, right_index):
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

    return find_all_occurences(numbers_list, number_to_find, left_index, right_index)





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




