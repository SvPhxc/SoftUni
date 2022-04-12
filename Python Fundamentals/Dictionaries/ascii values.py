words = input().split(", ")
ascii_nums = {word:ord(word) for word in words}
print(ascii_nums)