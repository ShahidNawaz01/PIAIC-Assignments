stat = input('Enter your statement: ')
count = 0

for i in stat:
    count += 1

x = 0
y = count - 1
num_count = 0
for i in range(count//2):
    if stat[x] != stat[y]:
        print('Not palindrome!')
        break
    x += 1
    y -= 1
    num_count += 1
if num_count == (count//2):
    print('Palindrome')