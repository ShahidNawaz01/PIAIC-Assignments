stat = input('Please enter your statement: ')
vowels_list = ['a', 'e', 'i', 'o', 'u']
vowels_count = 0
count = 0

for char in stat.lower():
    if char in vowels_list:
        vowels_count += 1
    if char != '.' and char != ' ':
        count += 1
consonants = count - vowels_count
print(f'In your statement, there are {vowels_count} vowels and {consonants} consonants.')