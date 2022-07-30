stat = input('Enter your statement: ')
avoid_repetition = []

for i in stat:
    count = 0
    if i not in avoid_repetition:
        for y in stat:
            if i == y:
                count += 1
        print(f'In your statement, {i} is repeated {count} times')
    avoid_repetition.append(i)