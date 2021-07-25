


"""Merge sort 3"""
import operator


def merge(left, right, compare):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        mid = int(len(L) / 2)
        left = merge_sort(L[:mid], compare)
        right = merge_sort(L[mid:], compare)
        return merge(left, right, compare)


arr = [15, 5, 55, 6, 19, 8, 4, 3, 17, 6, 2]
print(merge_sort(arr))





"""Merge sort 2"""

# def mergesort(arr):
#     if len(arr) < 2:
#         return arr
#     result = []
#     mid = len(arr) // 2
#     a = arr[:mid]
#     b = arr[mid:]
#
#     I_half = mergesort(a)
#     II_half = mergesort(b)
#
#     i = j = k = 0
#
#     while i < len(I_half) and j < len(II_half):
#         if I_half[i] < II_half[j]:
#             result.append(I_half[i])
#             i += 1
#         else:
#             result.append(II_half[j])
#             j += 1
#         k += 1
#
#     result += I_half[i:]
#     result += I_half[j:]
#
#     return result
#
#
#
# arr = [15, 5, 55 ,6 ,19 ,8 ,4 ,3 ,17, 6, 2]
# print(mergesort(arr))





"""Merge sort 1"""

# def sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         a, b = arr[:mid], arr[mid:]
#         sort(a)
#         sort(b)
#         i = j = k = 0
#         while i < len(a) and j < len(b):
#             if a[i] < b[j]:
#                 arr[k] = a[i]
#                 i += 1
#             else:
#                 arr[k] = b[j]
#                 j += 1
#             k += 1
#
#         while i < len(a):
#             arr[k] = a[i]
#             i += 1
#             k += 1
#
#         while j < len(b):
#             arr[k] = b[j]
#             j += 1
#             k += 1
#
#         return a, b
#
#
# def merge(arr):
#     a, b = sort(arr)
#     i, j = 0, 0
#     for k in range(len(a)):
#         if a[i] < b[j]:
#             arr[k] = a[i]
#             i += 1
#         else:
#             arr[k] = b[j]
#             j += 1
#
#     return arr
#
#
# arr = [8, 6, 4, 5, 7, 2, 3, 1]
# print(merge(arr))



"""Karatsuba multiplication"""
def Karatsuba(x, y):
    a = int(str(x)[:2])
    b = int(str(x)[2:])
    c = int(str(y)[:2])
    d = int(str(y)[2:])

    step_1 = a * c
    step_2 = b * d
    step_3 = (a + b) * (c + d)
    step_4 = step_3 - step_2 - step_1
    # step_5 =

    print(step_1)
    print(step_2)
    print(step_3)
    print(step_4)

    # return step_4




# x = 5678
# y = 1234
# print(Karatsuba(x, y))

# print("1.50" == str(1.50))











"""Mnożenie pod kreską"""


def memory_add(result, memory):
    for i in range(len(result) - 1, -1, -1):
        for j in range(len(result[0]) - 1, -1, -1):
            result[i][j] = memory[i][j] + result[i][j]
            if result[i][j] > 9:
                memo, result[i][j] = int(str(result[i][j])[0]), int(str(result[i][j])[1])
                memory[i][j - 1] = memo + memory[i][j - 1]

    return result


def final_add(result):
    len_assertion(result)
    f_result = []
    k = len(result[0]) - 1
    s = 0

    for i in range(len(result[0]) - 1, -1, -1):
        for j in range(len(result)):
            s += result[j][k]
        f_result.insert(0, s)
        k -= 1
        s = 0

    for i in range(len(f_result) - 1, -1, -1):
        if f_result[i] > 9:
            memo, f_result[i] = int(str(f_result[i])[0]), int(str(f_result[i])[1])
            f_result[i - 1] = memo + f_result[i - 1]

    return f_result


def len_assertion(result):
    longest = max([len(i) for i in result])

    for i in range(len(result)):
        while len(result[i]) < longest:
            result[i].insert(0, 0)

    return result


def grade_mult(x, y):
    x = str(x)
    y = str(y)

    result = [[] for _ in range(len(y))]
    memory_1 = [[0] for _ in range(len(y))]

    for r_ind, i in enumerate(reversed(y)):
        [memory_1[r_ind].append(0) for _ in range(r_ind) if r_ind > 0]
        [result[r_ind].append(0) for _ in range(r_ind) if r_ind > 0]
        for c_ind, j in enumerate(reversed(x)):
            k = int(i) * int(j)
            k = k + memory_1[r_ind][c_ind]
            if k > 9:
                memo, k = int(str(k)[:-1]), int(str(k)[-1])
                result[r_ind].insert(0, k)
                memory_1[r_ind].insert(0, memo)
            else:
                result[r_ind].insert(0, k)
                memory_1[r_ind].insert(0, 0)

        if len(result[r_ind]) < len(memory_1[r_ind]):
            result[r_ind].insert(0, 0)

    result = memory_add(result, memory_1)
    result = final_add(result)

    return int(''.join([str(i) for i in result]))


x = 56784578945789457894578
y = 123455555999991

# print(grade_mult(x, y))
# print(56784578945789457894578 * 123455555999991)


