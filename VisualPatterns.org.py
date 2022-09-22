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
# n = 5
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
# n = 6
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
# n = 7
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
# n = 9
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


# def vis9(n):
#     return '*' * n + '\n' + '*' * (n + 1) + '\n' + '*' * (n + 2) + '\n'
#
#
# print('\nvisual 9\n\n')
# n = 43
# for i in range(1, n + 1):
#     print(vis9(i), len(vis9(i)) - vis9(i).count('\n'))


########################################


# def vis10(n):
#     return '*' * (n + 1) + '\n' + '*' * n + '\n'
#
#
# print('\nvisual 10\n\n')
# n = 43
# for i in range(n):
#     print(vis10(i), len(vis10(i)) - vis10(i).count('\n'))


########################################


# def vis11(n, result=''):
#     while n <= 43:
#         result = ('*' + '\n') * n + '*' * (n + 1) + '\n'
#         n += 1
#         return vis11(n, result)
#     return result
#
#
# print('\nvisual 11\n\n')
# n = 1
# print(vis11(n), len(vis11(n)) - vis11(n).count('\n'))


########################################


# def vis12(n, result=''):
#     while n <= 43:
#         result = ('O' * (n + 1) + '\n') * (n + 1)
#         n += 1
#         return vis12(n, result)
#     return result
#
#
# print('\nvisual 12\n\n')
# n = 1
# print(vis12(n), len(vis12(n)) - vis12(n).count('\n'))


########################################


# def vis13(n, result=''):
#     while n <= 43:
#         result += 'O' * n + '\n'
#         n += 1
#         return vis13(n, result)
#     return result
#
#
# print('\nvisual 13\n\n')
# n = 1
# print(vis13(n), len(vis13(n)) - vis13(n).count('\n'))


########################################


# def vis14(n):
#     nl = '\n'
#     return f"O\n{('O' * n + nl) * 6}"
#
#
# print('\nvisual 14\n\n')
# n = 43
# for i in range(1, 1 + n):
#     print(vis14(i), len(vis14(i)) - vis14(i).count('\n'))


########################################


# def vis15(n, result=''):
#     s = u"\u2588"
#     nl = '\n'
#     result += f""" o{nl}o{s}o{nl}"""
#     return result * n + ' o'
#
#
# print('\nvisual 15\n\n')
# n = 43
# print(vis15(n))
# print(vis15(n).count('o'))


########################################


# def vis16_it(n, result=''):
#     for i in range(n + 1):
#         result += ' ' * (n - i) + '^' * (i + i - 1) + '\n'
#     return result
#
#
# print('\nvisual 16\n\n')
# n = 43
# print(vis16_it(n))
# print(vis16_it(n).count('^'))


########################################


# def vis16_rec(n, result=''):
#     m = 43
#     while n <= 43:
#         result += ' ' * (m - n) + '^' * (n + n - 1) + '\n'
#         n += 1
#         return vis16_rec(n, result)
#     return result
#
#
# print('\nvisual 16\n\n')
# n = 1
# print(vis16_rec(n))
# print(vis16_rec(n).count('^'))


########################################


# def vis17(n):
#     square = "\u2588"
#     return (' ' * n + square + '\n') * n + square * (n + n + 1) + '\n'
#
#
# print('\nvis17\n\n')
# n = 4
# for i in range(n):
#     print(vis17(i))
# print(vis17(n).count('\u2588'))


########################################


# def vis18(n):
#     sq = "\u2588"
#     return sq + '\n' + sq * 2 + (''.join([sq + '\n' + '  ' * (i + 1) + sq * 2 for i in range(n - 1)]))
#
#
# print('\nvis18\n\n')
# n = 43
# print(vis18(n))
# print(vis18(n).count('\u2588'))


########################################


# def vis19(n):
#     result = ''
#     for i in range(1, n + 1):
#         result = ' *' + ' ' * i + ('\n' + '*' * (i + 2)) * i + '\n *' + ' ' * i + '\n'
#     return result
#
#
# print('\nvis19\n\n')
# n = 3
# for i in range(n + 1):
#     print(vis19(i), vis19(i).count('*'))
#     print()


########################################


def vis20(n, result=''):
    while n <= 43:
        result += ('o' + ('oo' * n) + '\n') * n + '\n'
        n += 1
        return vis20(n, result)
    else:
        return result


print('\nvis20\n\n')
i = 43
print(vis20(i), vis20(i).count('o'))


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
