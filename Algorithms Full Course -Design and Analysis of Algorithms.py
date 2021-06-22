

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
    print(to_move)
    return result


x = 151
y = 152
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
