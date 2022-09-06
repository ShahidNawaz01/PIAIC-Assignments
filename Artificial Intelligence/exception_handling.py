while True:
    num = input('Enter any number: ')
    try:
        num = int(num)
        print('Valid input!')
        break
    except:
        print('Invalid input!')
        continue