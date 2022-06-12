n = int(input())

matrix = []

for _ in range(n):
    new_row = [int(x) for x in input().split(' ')]
    matrix.append(new_row)

result = 0
for i in range(n):
    result += matrix[i][i]
print(result)

'''
3
11 2 4
4 5 6
10 8 -12

3
1 2 3
4 5 6
7 8 9

'''