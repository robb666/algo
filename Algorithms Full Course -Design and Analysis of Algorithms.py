

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


def final_add(): pass


def grade_mult(x, y):
    x = str(x)
    y = str(y)

    result = [[] for _ in range(len(y))]
    memory_1 = [[0] for _ in range(len(y))]
    fresult = [[] for _ in range(len(y))]

    print(x, y)
    k = 0
    memo = 0
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
                memo, k = int(str(k)[:-1]), int(str(k)[-1])
                result[r_ind].insert(0, k)
                memory_1[r_ind].insert(0, memo)

            else:
                result[r_ind].insert(0, k)
                memory_1[r_ind].insert(0, 0)

        if len(result[r_ind]) < len(memory_1[r_ind]):
            result[r_ind].insert(0, 0)

    """dodać jedno jak w result zero do pomieci z tyłu"""

    # memory_add(result, memory_1)


        # if len(x) - 1 == c_ind and len(result[r_ind]) > len(memory_1[r_ind]):
        #     result[r_ind].insert(0, 0)

    # for i in range(len(result)):
    #     if memo + memory_1[0][0] + result[0][0] > 9:
    #         result[i].insert(0, memory_1[0][0])
    #
    #     if len(result[i]) < len(memory_1[i]):
    #         result[i].insert(0, 0)




    print(memory_1)
    print(result)


x = 99
y = 99

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
