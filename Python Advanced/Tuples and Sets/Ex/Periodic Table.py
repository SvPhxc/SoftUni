n = int(input())

result = set()

for _ in range(n):
    symbol = set(input().split(' '))
    result = result.union(symbol)

for i in result:
    print(i)

# 4
# Ce O
# Mo O Ce
# Ee
# Mo
