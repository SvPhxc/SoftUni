# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU

n = int(input())
parking_lot_logs = [input().split(', ') for _ in range(n)]

parking_lot = set()

for direction, car_num in parking_lot_logs:
    if direction == "IN":
        parking_lot.add(car_num)
    else:
        parking_lot.remove(car_num)
if parking_lot:
    [print(car_num) for car_num in parking_lot]
else:
    print("Parking Lot is Empty")