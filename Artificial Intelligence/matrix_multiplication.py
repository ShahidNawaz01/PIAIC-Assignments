row1 = int(input('Enter the no. of rows of 1st matrix: '))
col1 = int(input('Enter the no. of columns of 1st matrix: '))
row2 = int(input('Enter the no. of rows of 2nd matrix: '))
col2 = int(input('Enter the no. of columns of 2nd matrix: '))
matrix1 = list()
matrix2 = list()
prod_matrix = list()
help_list = list()

if col1 == row2:
    for rows in range(row1):
        help_list = list()
        for cols in range(col1):
            i = int(input(f'Enter [{rows}][{cols}] value of 1st matrix: '))
            help_list.append(i)
        matrix1.append(help_list)
    for rows in range(row2):
        help_list = list()
        for cols in range(col2):
            i = int(input(f'Enter [{rows}][{cols}] value of 2nd matrix: '))
            help_list.append(i)
        matrix2.append(help_list)

    for rows in range(row1):
        help_list = list()
        for cols in range(col2):
            sum = 0
            for i in range(col1):
                sum += matrix1[rows][i]*matrix2[i][cols]
            help_list.append(sum)
        prod_matrix.append(help_list)
else:
    print('Columns of matrix 1 should be equal to rows of matrix 2.')

print(prod_matrix)