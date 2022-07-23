list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 7, 8]
com_elements = []

for x in list1:
    for y in list2:
        if x == y:
            com_elements.append(x)

print('Common elements b/w two lists are:', com_elements)