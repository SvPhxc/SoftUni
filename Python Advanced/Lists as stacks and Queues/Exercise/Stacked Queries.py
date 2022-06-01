rotations = int(input())
nums = []
for i in range(rotations):
    command = input().split(' ')
    if int(command[0]) == 1:
        nums.append(int(command[1]))
    elif int(command[0]) == 2 and nums:
        nums.pop()
    elif int(command[0]) == 3 and nums:
        print(max(nums))
    elif int(command[0]) == 4 and nums:
        print(min(nums))
reversed_str = []
while nums:
    reversed_str.append(str(nums.pop()))

print(', '.join(reversed_str))
'''
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4


10
2
1 47
1 66 
1 32
4
3 
1 25 
1 16 
1 8 
4

'''
