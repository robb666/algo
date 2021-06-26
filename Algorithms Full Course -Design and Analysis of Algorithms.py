

def grade_mult(x, y):
    result = [[] for _ in range(len(str(y)))]
    memory_1 = []
    for c_ind, i in enumerate(reversed(str(y))):
        for j in reversed(str(x)):
            k = int(i) * int(j)
            if k > 9:
                move, k = int(str(k)[:-1]), int(str(k)[-1])
                result[c_ind].insert(0, k)
                memory_1.append(move)
                print(memory_1)
                continue
            if memory_1:
                k = k + memory_1.pop()
                result[c_ind].insert(0, k)
            else:
                result[c_ind].insert(0, k)
    try:
        k = memory_1.pop()
        result[0].insert(0, k)
    except:
        pass

    matrix = result
    print(matrix)
    row_len = len(matrix)
    col_len = len(matrix[0])

    arr = []
    for k in range(col_len - 1, 0, -1):
        i = 0
        j = k
        sum1 = 0
        while j <= col_len - 1:
            sum1 += matrix[i][j]
            i += 1
            j += 1
        arr.insert(0, sum1)

    for k in range(len(matrix)):
        i = k
        j = 0
        sum2 = 0
        while i <= row_len - 1:
            sum2 += matrix[i][j]
            i += 1
            j += 1
        arr.insert(0, sum2)

    final_result = []
    memory_2 = []
    for i in reversed(arr):
        if i > 9:
            move, i = int(str(i)[:-1]), int(str(i)[-1])
            final_result.insert(0, i)
            memory_2.append(move)
            continue

        if memory_2:
            i = i + memory_2.pop()
            final_result.insert(0, i)
        else:
            final_result.insert(0, i)

    try:
        k = memory_2.pop()
        final_result.insert(0, k)
    except:
        pass

    return ''.join([str(i) for i in final_result])



x = 12345
y = 5

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
