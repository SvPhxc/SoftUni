nums = input().split(' ')
nums2 = []
result = []
for i in nums:
    nums2.append(i)

for x in nums:
    result.append(nums2.pop())

for c in result:
    print(c, end=' ')
