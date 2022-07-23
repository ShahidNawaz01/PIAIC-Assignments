import random
x = random.randint(1, 10)

for i in range(3):
    guess = int(input('Guess any number b/w 1 to 10: '))
    if guess == x:
        print('You won!')
        break
    else:
        print('Try guessing again.')
if guess != x:
    print('Better luck next time!')