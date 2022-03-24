keys = input().split(", ")
subs = input()
final = [x for x in keys if x in subs]
print(final)