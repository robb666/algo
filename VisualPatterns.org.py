# # https://www.visualpatterns.org/

#
#
# def vis1(n):
#     return ('O' * n + '\n') * n
#
#
# print('\nvisual 1' + '\n\n')
# [print(vis1(n)) for n in range(4)]
#
#
# ########################################
#
#
# def vis2(n):
#     return (' ' * (n - 1) + 'O' + '\n') * (n - 1) + 'O' * n
#
#
# print('\nvisual 2\n\n')
# n = 4
# [print(vis2(i) + '\n') for i in range(n)]
#
#
# ########################################
#
#
# def vis3(n):
#     return ''.join(['O' * n + '\n' for n in range(n)])
#
#
# print('\nvisual 3\n\n')
# n = 5
# [print(vis3(i)) for i in range(2, n)]


########################################


def vis4(n):
    result = ''
    for i in range(0, n + 1):
        result += ' ' * i + 'O' + ' ' * (((n - i) * 2) - 1) + 'O' + ' ' * i + '\n'
        if i == n - 1:
            break
    for i in reversed(range(0, n + 1)):
        if i == n:
            result += ' ' * i + 'O' + ' ' * (((n - i) * 2) - 1) + '' + ' ' * i + '\n'
            continue
        result += ' ' * i + 'O' + ' ' * (((n - i) * 2) - 1) + 'O' + ' ' * i + '\n'

    return result


print('\nvisual 4\n\n')
n = 3
for num in range(1, n + 1):
    print(vis4(num))


########################################


# def vis32(n, result=''):
#     for _ in range(n + 1):
#         result += 'O' * n + '\n'
#     return result


# print('\n' * 4 + 'visual 32')
# for n in range(4):
#     print(vis32(n))


########################################



v = 8

print(
                                        f"""\n\n\n
                                           /
                                          / \\
                                         /   \\
                                        /     \\
                                       |   {v}   | 
                                        \\     /
                                         \\   /
                                          \\ /
                                           /
                                        """
)
