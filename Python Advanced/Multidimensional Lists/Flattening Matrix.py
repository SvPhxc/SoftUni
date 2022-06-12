n = int(input())
result = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    result.append(row)


print([num for sub in result for num in sub])

'''
2
1, 2, 3
4, 5, 6

'''