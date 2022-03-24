nums = input().split(" ")
int_nums = []
for i in nums:
    int_nums.append(int(i))
print(f"The minimum number is {min(int_nums)}")
print(f"The maximum number is {max(int_nums)}")
print(f"The sum number is: {sum(int_nums)}")
