value = int(input('Enter the value of which table is required: '))
iter = int(input('Enter the value upto which table is required: '))
for i in range(1,iter+1):
    print(f'{value} * {i} = {value*i}')