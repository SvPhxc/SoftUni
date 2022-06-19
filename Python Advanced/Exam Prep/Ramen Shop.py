'''
ramen
customers

while customers or ramen
    ramen_bow
    customer
    if ramen_bow = customer
        remove both

    elif ramen_bow > customer
        ramen -= customer
        remove customer
        add ramen back to final

    elif ramen_bow < customer
        customer -= ramen_bow
        remove ramen
        add customer back to start

if not customers
    print served all
    if ramen
        print bowls left

else
    print out of ramen
    print customers left



14, 25, 37, 43, 19
58, 23, 37

30, 13, 45
70, 25, 55, 15


30, 25
20, 35

'''

from collections import deque

ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])


while ramen and customers:
    ramen_bowl = ramen.pop()
    customer = customers.popleft()

    if ramen_bowl == customer:
        continue

    elif ramen_bowl > customer:
        ramen_bowl -= customer
        ramen.append(ramen_bowl)
        continue

    elif ramen_bowl < customer:
        customer -= ramen_bowl
        customers.appendleft(customer)
        continue

if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
