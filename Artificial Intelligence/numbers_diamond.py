number = int(input('Enter any number: '))
pattern_def = number
half_pattern_def = number

for x in range(number):
    output = ''
    for y in range(1, 2*number):
        if y == pattern_def or y == half_pattern_def:
            output = output + str(pattern_def)
        else:
            output = output + ' '
    print(output)
    pattern_def -= 1
    half_pattern_def += 1

pattern_def = 2
half_pattern_def = 2*number - 2
for x in range(number - 1):
    output = ''
    for y in range(1, 2*number):
        if y == pattern_def or y == half_pattern_def:
            output = output + str(pattern_def)
        else:
            output = output + ' '
    print(output)
    pattern_def += 1
    half_pattern_def -= 1
