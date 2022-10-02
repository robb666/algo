from collections import deque

stack = deque()
# print(dir(stack))

# Can use:

# stack.append('https://www.cnn.com/')
# stack.append('https://www.cnn.com/world')
# stack.append('https://www.cnn.com/india')
# stack.append('https://www.cnn.com/china')


# ..OR


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        return self.container.append(value)

    def pop(self):
        return self.container.pop()

    def popleft(self):
        return self.container.popleft()

    def peak(self):
        return self.container[-1]

    def bottom(self):
        return self.container[0]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)




print('\n\n\n')


# ex.1


def revind(string):
    stack = deque()
    rev_string = ''
    for letter in string:
        stack.append(letter)

    while stack:
        rev_string += stack.pop()

    return rev_string


string = 'Wi ar in de simiulejszyn!'
print(revind(string))

print('\n\n\n')




# ex. 2


def is_balanced(expression):

    s = Stack()

    brackets = ('(', ')', '[', ']', '{', '}')

    x = ('(', ')')
    y = ('[', ']')
    z = ('{', '}')

    for par in expression:
        if par in brackets:
            s.push(par)

    while not s.is_empty():
        par_r = s.pop()

        if not s.is_empty():
            par_l = s.container[0]

            if par_r in x and par_l == '(':
                s.popleft()
            elif par_r in y and par_l == '[':
                s.popleft()
            elif par_r in z and par_l == '{':
                s.popleft()
            else:
                return False
        else:
            return False
    return True


exp = '{[{(((((2 ** 2)))))}]}'


print(is_balanced(exp))


# def is_match(ch1, ch2):
#     match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#     return match_dict[ch1] == ch2
#
#
# def is_balanced(s):
#     stack = Stack()
#     for ch in s:
#         if ch == '(' or ch == '{' or ch == '[':
#             stack.push(ch)
#         if ch == ')' or ch == '}' or ch == ']':
#             if stack.size() == 0:
#                 return False
#             if not is_match(ch, stack.pop()):
#                 return False
#
#     return stack.size() == 0
#
#
# if __name__ == '__main__':
#     exp = '{[{(((((2 ** 2)))))}]}'
#
#     print(is_balanced(exp))

