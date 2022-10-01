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

    for par in expression:
        if par in brackets:
            s.push(par)

    x = ('(', ')')
    y = ('[', ']')
    z = ('{', '}')

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


exp = '{[{(((((2 ** 2)))))}}'


print(is_balanced(exp))
