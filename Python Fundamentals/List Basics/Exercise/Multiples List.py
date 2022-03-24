num1 = int(input())
num2 = int(input())
nums = list()
for num in range(1, num2 + 1):
    nums.append(num * num1)
print(nums)