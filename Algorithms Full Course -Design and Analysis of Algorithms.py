

def grade_mult(x, y):
    result = []
    for i in str(x):
        for j in str(y):
            h = int(i) * int(j)
            result.insert(0, h)
    return result


y = 152
x = 151
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