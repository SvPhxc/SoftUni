number = int(input())
searched_word = input()
strings = list()
filtered = list()
for i in range(number):
    current_word = input()
    strings.append(current_word)
    if searched_word in current_word:
        filtered.append(current_word)

print(strings)
print(filtered)