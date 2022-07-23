import random
x = random.randint(1, 10)

for i in range(3):
    guess = int(input('Guess any number b/w 1 to 10: '))
    if guess == x:
        print('You won!')
        break
if guess != x:
    print('Try again!')