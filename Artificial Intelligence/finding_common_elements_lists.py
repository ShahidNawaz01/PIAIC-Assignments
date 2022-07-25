list1 = [1, 2, 3, 4, 5, 1, 2, 3]
list2 = [3, 4, 5, 1, 7, 8, 1, 2]

# program to print common elements without duplication
com_elements1 = []
for x in list1:
    for y in list2:
        if x == y:
            if y not in com_elements1:
                com_elements1.append(y)
print('Common elements (without duplicates):', com_elements1)

# program to print common elements (also counting of elements 
# even if they appear multiple times in both lists)
com_elements2 = []
numbers_list1 = len(list1)
numbers_list2 = len(list2)

for x in range(numbers_list1):
    y = 0
    while y < numbers_list2:
        if list1[x] == list2[y]:
            com_elements2.append(list2[y])
            list2.remove(list2[y])
            break
        y = y + 1
    numbers_list2 = len(list2)
print('Common elements (allowing multiple appearances of elements):', com_elements2)