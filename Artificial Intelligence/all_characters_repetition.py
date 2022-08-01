stat = input('Enter your statement: ')
avoid_repetition = []

for i in stat.lower():
    count = 0
    if i not in avoid_repetition:
        for y in stat.lower():
            if i == y:
                count += 1
        print(f"In your statement, '{i}' is repeated {count} times")
    avoid_repetition.append(i)