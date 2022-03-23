num = int(input())
total_sum = 0
for n in range(num):
    symbol = input()
    total_sum += ord(symbol)
print(F'The sum equals: {total_sum}')