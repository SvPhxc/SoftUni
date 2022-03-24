text = input().split(' ')
for i in text:
    if len(i) % 2 == 0:
        print(i)
    else:
        continue
