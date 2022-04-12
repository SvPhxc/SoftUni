text = input().split(' ')
result = ''
for i in text:
    word = len(i)
    result += i * word
print(result)