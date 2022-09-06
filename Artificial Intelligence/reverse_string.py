# storing each character of a string into a list and apply the reverse function
string = input('Enter a string: ')
str_list = list(string)
str_list.reverse()
reverse_str = ''
for i in str_list:
    reverse_str += i
print(reverse_str)

# reversing string using recursive loop
def rev_str(string):
    if len(string) == 0:
        return string
    else:
        return rev_str(string[1:]) + string[0]
print(rev_str(string))

# Using Python function
print(string[::-1])