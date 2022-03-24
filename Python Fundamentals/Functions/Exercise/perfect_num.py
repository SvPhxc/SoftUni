num = int(input())
nums = []
for i in range(1, num):
    if num % i == 0:
        nums.append(int(i))
    else:
        continue
if sum(nums) == num:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")