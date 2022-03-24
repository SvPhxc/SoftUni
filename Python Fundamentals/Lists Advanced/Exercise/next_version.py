version = input().split(".")
version = int(''.join(version)) + 1
result = [str(num) for num in str(version)]
print('.'.join(result))
