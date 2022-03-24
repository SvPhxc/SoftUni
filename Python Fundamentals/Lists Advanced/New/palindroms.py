strings = input().split(' ')
searched_palindrome = input()
palindroms = [word for word in strings if word == ''.join(reversed(word))]
print(f"{palindroms}")
print(f"Found palindrome {palindroms.count(searched_palindrome)} times")