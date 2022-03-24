vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
no_vowels_list = [ch for ch in text if ch not in vowels]

print("".join(no_vowels_list))