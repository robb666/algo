
def arr_max(arr):
    pass

arr = [1, 2, 3, 44, 6]
print(arr_max(arr))


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



