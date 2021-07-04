
"""Mnożenie pod kreską"""
def memory_add(result, memory):
    memo = 0
    for i in range(len(result) - 1, -1, -1):
        for j in range(len(result[0]) - 1, -1, -1):
            result[i][j] = memory[i][j] + result[i][j]
            if result[i][j] > 9:
                memo, result[i][j] = int(str(result[i][j])[0]), int(str(result[i][j])[1])
                memory[i][j - 1] = memo + memory[i][j - 1]

    if memory[0][0] + result[0][0] > 9:
        result[0].insert(0, memo)

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


x = 54321
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
