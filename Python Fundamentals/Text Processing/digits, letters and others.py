text = input()
letter = ''
digit = ''
other = ''
for i in text:
    if i.isalpha():
        letter += i
    elif i.isdigit():
        digit += i
    else:
        other += i
print(digit)
print(letter)
print(other)