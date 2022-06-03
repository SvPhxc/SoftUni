from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split(' ')])

print(max(orders))

while orders:
    if orders[0] > food:
        break
    else:
        food -= orders.popleft()

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")

'''
348
20 54 30 16 7 9

499
57 45 62 70 33 90 88 76 100 50

'''