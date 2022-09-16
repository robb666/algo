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
    for i in range(n+1):  # nieparzyste
        result += ' ' * i + 'O' + '  ' * (n - i) + 'O' + ' ' * i +'\n'
    result += ' ' * n + 'O'
    return result


print('\nvisual 4\n\n')
# [print(vis4(n)) for n in range(4)]
n = 4
print(vis4(n))

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
