
capitalized = 'DOKUMENTACJA'

print(capitalized)

folded = capitalized.casefold()

print(folded)

centered = folded.center(18, '/')

print(centered)
print('//\,.>'.isprintable())
print('   '.isspace())

print('BANANA'.isupper())
print('baNana'.isupper())

to_join = ['Where is ', 'python: ', '0152', '5', ' 9']
print(''.join(to_join).center(40, '-'))


str_to_just = 'python not java'

print(str_to_just.rjust(40, '*'))
print(str_to_just.ljust(40, '*'))

print('BMW 535d, 2993 cm3'.rstrip(' cm3'))
print('BMW 535d, 2993 cm3'.removesuffix(' cm3'))
print('BMW 535d, 2993 cm3'[:-4])


def stripper(obj):
    return obj.removesuffix(',/?><\;][cm3')


arr = ['2993 cm3', 'def][', 'ijk>', 'ooop.,/?><\;][cm3']

strriped = map(stripper, arr)
strr_list = list(strriped)
print(strr_list)


def capital(obj):
    return obj.upper()

arr1 = ['gosia', 'zosia', 'basia', 'kasia']
mpp = list(map(capital, arr1))
print(mpp)

for i in arr1:
    print(capital(i))

print('+002'.zfill(6))

dict = {"a": "123", "b": "456", "c": "789"}
string = ""
print(string.maketrans(dict))

str1 = 'XXXxxxpol'.partition('x')
print(str1)
str1rep = 'XXXxxxpol'.rpartition('x')
print(str1rep)


str2 = 'XXXxxxpol'
print(str2.rfind('x'))

import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(), s)

s = titlecase("they're bill's friends.")
print(s)

result = re.sub(r'(Bill)\'s Friends', r'\1', s)
print(result)



# return a str, return a copy
# maketrans




























