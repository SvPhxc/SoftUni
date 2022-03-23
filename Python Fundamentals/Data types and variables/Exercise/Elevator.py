n = int(input())
p = int(input())
c = int(n / p)
if c > 0:
    if n % p != 0:
        c += 1
    print(c)
elif c < 1:
    print('1')