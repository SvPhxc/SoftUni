num = int(input())
for i in range(0, num):
    for b in range(0, num):
        for c in range(0, num):
            print(f"{chr(97 + i)}{chr(97 + b)}{chr(97 + c)}")