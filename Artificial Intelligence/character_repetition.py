stat = input('Enter any statement: ')
char = input('Enter the character of which you want to see repition: ')
count = 0

for i in stat.lower():
    if i == char.lower():
        count += 1

print(f"Character '{char}' is repeated {count} times in above statement.")