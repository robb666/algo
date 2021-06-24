

def grade_mult(x, y):
    result = [[] for column in range(len(str(y)))]
    to_move = []
    for c_ind, i in enumerate(reversed(str(y))):
        for r_ind, j in enumerate(reversed(str(x))):
            h = int(i) * int(j)
            if h > 9:
                move, h = int(str(h)[:-1]), int(str(h)[-1])
                result[c_ind].insert(0, h)
                to_move.insert(0, move)
                continue
            if to_move:
                h = h + to_move.pop()
                result[c_ind].insert(0, h)
            else:
                result[c_ind].insert(0, h)
    print(len(result))

    sum1 = sum([result[0][2]])
    sum2 = sum([result[0][1], result[1][2]])
    sum3 = sum([result[0][0], result[1][1], result[2][2]])
    sum4 = sum([result[1][0], result[2][1]])
    sum5 = sum([result[2][0]])

    arr = []
    for row in range(len(result)):
        for column in range(len(result) - 1, - 1, - 1):
            arr.append(result[row][column])
            try:
                arr.append(result[row + 1][column + 1])
                arr.append(result[row + 2][column + 2])
            except:
                pass

        print(arr)
    print(arr)

    return result  #, sum5, sum4, sum3, sum2, sum1



x = 151
y = 152
print(grade_mult(x, y))


n = 3
print([(n - i - 1, i) for i in range(n)])


""""""
matrix = [[3, 0, 2],
          [7, 5, 5],
          [1, 5, 1]]
# print(len(matrix))
arr = []
for row in range(len(matrix)):
    for column in range(len(matrix) - 1, - 1, - 1):
        arr.append(matrix[row][column])
        try:
            arr.append(matrix[row + 1][column + 1])
            arr.append(matrix[row + 2][column + 2])
        except:
            pass

    print(arr)
print(arr)
""""""





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
