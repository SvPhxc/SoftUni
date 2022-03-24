rooms = int(input())
free = 0
needed = 0
for i in range(1, rooms + 1):
    info = input().split(' ')
    chairs = len(info[0])
    visitors = int(info[1])
    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {i}")
        needed += visitors - chairs
    else:
        free += chairs - visitors
if needed == 0:
    print(f"Game On, {free} free chairs left")

