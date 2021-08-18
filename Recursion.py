
def rec_bs(arr, i):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    guess = arr[mid]
    if arr and guess == i:
        return arr[0]
    if i < guess:
        return rec_bs(arr[:mid - 1], i)
    if i > guess:
        return rec_bs(arr[mid + 1:], i)
    return False


arr = [1, 2, 3, 4, 5]
print(rec_bs(arr, 5))


def arr_max(arr, max_):
    if not arr:
        return max_
    next_ = arr.pop()
    if next_ > max_:
        max_ = next_
    return arr_max(arr, max_)


# arr = [-3, 7, 52, 3, 44, 6, -3]
# max_from_arr = arr[0]
# print(arr_max(arr, max_from_arr))


def arr_len(arr):
    if not arr:
        return 0
    else:
        arr.pop()
        return 1 + arr_len(arr)


# arr = [1, 2, 3, 4, 6]
# print(arr_len(arr))


def arr_sum(arr):
    if arr:
        return arr.pop() + arr_sum(arr)
    else:
        return 0


# arr = [-1, -2, 5, 6]
# print(arr_sum(arr))


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


# print(fact(3))




