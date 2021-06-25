

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

    matrix = result

    row_len = len(matrix)
    col_len = len(matrix[0])

    arr = []

    for k in range(col_len - 1, 0, -1):
        i = 0
        j = k
        while j <= col_len - 1:
            sum1 = matrix[i][j]
            arr.insert(0, sum1)
            i += 1
            j += 1

    for k in range(len(matrix)):
        i = k
        j = 0
        while i <= row_len - 1:
            arr.insert(0, matrix[i][j])
            i += 1
            j += 1

    print(arr)

    final_result = []
    final_to_move = []
    for i in arr:
        if i > 9:
            move, h = int(str(i)[:-1]), int(str(i)[-1])
            final_result.insert(0, h)
            final_to_move.insert(0, move)
            continue


            ;;;
        if to_move:
            h = h + to_move.pop()
            result[c_ind].insert(0, h)
        else:
            result[c_ind].insert(0, h)


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
            if column == 0:
                # for column in range(len(matrix) - 1, - 1, - 1):
                    arr.append(matrix[1][0])
                    arr.append(matrix[2][1])
                    arr.append(matrix[2][0])
                    break
        except:
            pass

    # print(arr)
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
