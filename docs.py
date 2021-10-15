
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

# return a str, return a copy