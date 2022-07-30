number = int(input('Enter any number b/w 1 to 10: '))

for x in range(1,number+1):
    y = 1
    output = ''
    while y <= number:
        output += str(y)
        y = y + 1
    print(output)
    number -= 1