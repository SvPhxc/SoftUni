from collections import deque

bees = deque([int(x) for x in input().split(' ')])
nectars = [int(x) for x in input().split(' ')]
symbols = deque(input().split(' '))
honey_total = 0
while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    if nectar < bee:
        bees.appendleft(bee)
        continue
    if nectar == 0:
        continue

    symbol_nectar = symbols.popleft()
    if symbol_nectar == '+':
        honey_total += abs(bee + nectar)
    elif symbol_nectar == '-':
        honey_total += abs(bee - nectar)
    elif symbol_nectar == '*':
        honey_total += abs(bee * nectar)
    elif symbol_nectar == '/':
        honey_total += abs(bee / nectar)

print(f"Total honey made: {honey_total}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
elif nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")


'''
20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /

30
15 9 5 150 8
* + + * -

'''
