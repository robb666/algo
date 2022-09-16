# https://www.visualpatterns.org/



def vis1(n):
    return ('O' * n + '\n') * n


print('\nvisual 1' + '\n\n')
[print(vis1(n)) for n in range(4)]


########################################



def vis2(n):
    return (' ' * (n - 1) + 'O' + '\n') * (n - 1) + 'O' * n


print('\nvisual 2\n\n')
[print(vis2(i) + '\n') for i in range(4)]



########################################



def vis3(n, result=''):
    # for i in range(n):
    #     result += ('O' * (i - 1) + '\n' + 'O' * n)
    # return result

    return 'O' + '\n' + 'o' * (n - 1)


print('\nvisual 3\n\n')
# for i in range(5):
print(vis3(3))
# [print(vis3(i)) for i in range(4)]





########################################




def vis32(n, result=''):
    for _ in range(n + 1):
        result += 'O' * n + '\n'
    return result


print('\n' * 4 + 'visual 32')
for n in range(4):
    print(vis32(n))
