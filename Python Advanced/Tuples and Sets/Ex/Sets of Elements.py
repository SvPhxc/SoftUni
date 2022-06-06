n, m = [int(x) for x in input().split(' ')]

first = set()
second = set()

for _ in range(n):
    first.add(int(input()))

for _ in range(m):
    second.add(int(input()))
result = first.intersection(second)
for num in result:
    print(num)    



# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5
