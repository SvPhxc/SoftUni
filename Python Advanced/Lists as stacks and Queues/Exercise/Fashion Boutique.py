clothes = [int(x) for x in input().split(' ')]
rack_cap = int(input())
cur_rack_cap = rack_cap
racks_needed = 1
while clothes:
    clothes_sum = clothes[-1]
    if clothes_sum > cur_rack_cap:
        racks_needed += 1
        cur_rack_cap = rack_cap

    else:
        cur_rack_cap -= clothes_sum
        clothes.pop()

print(racks_needed)

'''
5 4 8 6 3 8 7 7 9
16

'''