nums = input().split(", ")
positive = [i for i in nums if int(i) >= 0]
negative = [i for i in nums if int(i) < 0]
even = [i for i in nums if int(i) % 2 == 0]
odd = [i for i in nums if int(i) % 2 != 0]
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
