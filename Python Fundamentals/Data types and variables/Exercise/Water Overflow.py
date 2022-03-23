lines = int(input())
poured = 0
for i in range(lines):
    pouring = int(input())
    if pouring + poured <= 255:
        poured += pouring
        continue
    print("Insufficient capacity!")
print(poured)
