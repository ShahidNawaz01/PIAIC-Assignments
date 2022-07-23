import random
x = random.randint(1, 10)
guess = int(input('Guess any number b/w 1 to 10: '))
for i in range(2):
    if guess != x:
        guess = input('Guess again: ')
    else:
        print('You won!')
        break
if guess != x:
    print('You failed.')