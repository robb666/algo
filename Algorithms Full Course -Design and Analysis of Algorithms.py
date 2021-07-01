

def grade_mult(x, y):
    x = str(x)
    y = str(y)

    result = [[] for _ in range(len(y))]
    memory_1 = [[0] for _ in range(len(y))]
    fresult = [[] for _ in range(len(y))]
    # trailing_zeros = []
    #
    # for i in reversed(x):
    #     if i.startswith('0'):
    #         x = y.replace('0', '')
    #         trailing_zeros.append(0)
    #     else:
    #         break
    #
    # for i in reversed(y):
    #     if i.startswith('0'):
    #         y = y.replace('0', '')
    #         trailing_zeros.append(0)
    #     else:
    #         break
    #
    # print(trailing_zeros)
    print(x, y)
    for r_ind, i in enumerate(reversed(y)):
        [result[r_ind].append(0) for _ in range(r_ind) if r_ind > 0]
        for c_ind, j in enumerate(reversed(x)):
            print(memory_1)
            print(result)
            print(i, j)
            k = int(i) * int(j)
            k = k + memory_1[r_ind][c_ind]
            print(k)
            if k > 9:
                # result[r_ind][-1] = 0
                # result[r_ind].insert(0, 0)
                # memory_1[r_ind].append(0)
                memo, k = int(str(k)[:-1]), int(str(k)[-1])
                result[r_ind].insert(0, k)
                memory_1[r_ind].insert(0, memo)

    #
    #             print(memory_1)
    #             print(result)
    #
            else:
                result[r_ind].insert(0, k)
                memory_1[r_ind].insert(0, 0)
                if len(x) - 1 == c_ind and len(result[r_ind]) < len(memory_1[r_ind]):
                    result[r_ind].insert(0, 0)
    #
    # print(memory_1)
    # print(result)

    for i in range(len(result)):
        for j in range(len(result[0])):
            s = result[i][j] + memory_1[i][j]
            fresult[i].append(s)
    #
    #
    #
    matrix = fresult
    print(matrix)
    # row_len = len(matrix)
    # print(row_len)
    # col_len = len(matrix[0])
    # print(col_len)
    arr = []
    # if row_len > 1:
    #     for k in range(col_len - 1, 0, -1):
    #         i = 0
    #         j = k
    #         sum1 = 0
    #         while j <= col_len - 1:
    #             sum1 += matrix[i][j]
    #             i += 1
    #             j += 1
    #         arr.insert(0, sum1)
    #
    #     for k in range(len(matrix)):
    #         i = k
    #         j = 0
    #         sum2 = 0
    #         while i <= row_len - 1:
    #             sum2 += matrix[i][j]
    #             i += 1
    #             j += 1
    #         arr.insert(0, sum2)
    #
    #
    # print(matrix)
    # final_result = []
    # memory_2 = []
    # for k in reversed(arr):
    #     if k > 9:
    #         memo, k = int(str(k)[:-1]), int(str(k)[-1])
    #         final_result.insert(0, k)
    #         memory_2.append(memo)
    #         print(memory_1)
    #         print(result)
    #
    #     else:
    #         final_result.insert(0, k)
    #         if len(result) > len(memory_1):
    #             memory_2.insert(0, 0)
    #
    # return ''.join([str(i) for i in final_result])
    #
    # return ''.join([str(i) for i in fresult[0]])


x = 12345
y = 13

print(grade_mult(x, y))







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
