from collections import deque

pumps_count = int(input())
pumps = deque()
for _ in range(pumps_count):
    pumps.append([int(x) for x in input().split()])
for attempt in range(pumps_count):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break


'''
3
1 5
10 3
3 4


5
22 5
14 10
52 7
21 12
36 9
'''