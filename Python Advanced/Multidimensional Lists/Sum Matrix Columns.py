row, column = [int(x) for x in input().split(', ')]
matrix = []
for i in range(row):
    new_row = [int(x) for x in input().split(' ')]
    matrix.append(new_row)

result = []
for i in range(column):
    column_sum = 0
    for j in range(row):
        column_sum += matrix[j][i]
    result.append(column_sum)

[print(x) for x in result]

'''
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0

'''