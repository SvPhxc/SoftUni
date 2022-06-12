n = int(input())

matrix = []

for _ in range(n):
    matrix.append([x for x in input()])

symbol = input()
found = ()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            found += (i, j)
            break

if found != ():
    print(found)
else:
    print(f"{symbol} does not occur in the matrix")

'''
3
ABC
DEF
X!@
!

4
asdd
xczc
qwee
qefw
4

'''

