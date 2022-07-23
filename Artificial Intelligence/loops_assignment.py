import random
arr = []
total_sum = 0
greater_than_40 = []
sum_greater_than_40 = 0

# generating 100 random numbers and computing their sum
# meanwhile figuring out numbers greater than 40 and store them 
# in a separate list and also computing their sum
print('List of random numbers:')
for i in range(100):
    arr.append(random.randint(10,90))
    if arr[i] > 40:
        greater_than_40.append(arr[i])
        sum_greater_than_40 += arr[i]
    total_sum += arr[i]
    print(arr[i])

#figure out maximum and minimum values in a list of random numbers
maximum = arr[0]
minimum = arr[0]
for i in range(100):
    if arr[i] > maximum:
        maximum = arr[i]
    if arr[i] < minimum:
        minimum = arr[i]

print(f'Sum of 100 random numbers is: {total_sum}')
print(f'Average of 100 random numbers is: {total_sum/100}')
print(f'Maximum value out of 100 random values is: {maximum}')
print(f'Minimum value out of 100 random values is: {minimum}')
print(f'Numbers greater than 40: {len(greater_than_40)}')
print(f'Sum of numbers greater than 40: {sum_greater_than_40}')