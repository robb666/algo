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


# def vis4(n):
#     result = ''
#     for i in range(0, n + 1):
#         result += ' ' * i + 'O' + ' ' * (((n - i) * 2) - 1) + 'O' + ' ' * i + '\n'
#         if i == n - 1:
#             break
#     for i in reversed(range(0, n + 1)):
#         if i == n:
#             result += ' ' * i + 'O' + ' ' * (((n - i) * 2) - 1) + '' + ' ' * i + '\n'
#             continue
#         result += ' ' * i + 'O' + ' ' * (((n - i) * 2) - 1) + 'O' + ' ' * i + '\n'
#
#     return result
#
#
# print('\nvisual 4\n\n')
# n = 3
# for num in range(1, n + 1):
#     print(vis4(num))


########################################


# def vis5(n):
#     return (' ' * n + 'O' * (n + 1)) + \
#            ('\n' + ' ' * (n + 1) + 'O' * n) * (n - 1) + \
#            ('\n' + 'O' + ' ' * n + 'O' * (n * 1)) + \
#             '\n' + 'O' * (n + 2) + \
#            ('\n' + 'O' * (n + 1)) * (n - 1)
#
#
# print('\nvisual 5\n\n')
# n = 4
# for num in range(1, n + 1):
#     print(vis5(num) + '\n')


########################################


# def vis6(n):
#     result = ''
#     for i in range(n + 1):
#         result += ' ' * (n - i) + '^ ' * i + '\n'
#     return result
#
#
# print('\nvisual 5 \n\n')
# n = 3
# for i in range(1, n + 1):
#     print(vis6(i))


########################################


# def vis7(n):
#     return '**\n' * n + '*' * 3 + '\n'
#
#
# print('\nvisual 6\n\n')
# n = 3
# for i in range(n):
#     print(vis7(i))


########################################


# def vis8(n):
#     result = ''
#     for i in range(n):
#         result += '*' * (i + 1)
#         if i + 1 == n:
#             return result + '*\n'
#         result += '\n'
#     return result
#
#
# print('\nvisual 8\n\n')
# n = 3
# for i in range(1, n + 1):
#     print(vis8(i))


########################################


def vis9(n):
    return '*' * n + '\n' + '*' * (n + 1) + '\n' + '*' * (n + 2) + '\n'


print('\nvisual 9\n\n')
n = 43
for i in range(1, n + 1):
    print(vis9(i), len(vis9(i)) - vis9(i).count('\n'))


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
