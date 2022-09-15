



def vis1(n):
    result = ''
    for i in range(n + 1):
        result += 'O'

    return result


print('\nvisual1' + '\n\n')
for n in range(4):
    print(vis1(n))




def vis32(n):
    result = ''
    for _ in range(n + 1):
        result += 'O' * n + '\n'

    return result


print('\n' * 4 + 'visual32')
for n in range(4):
    print(vis32(n))