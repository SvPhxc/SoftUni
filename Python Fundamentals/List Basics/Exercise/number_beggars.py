nums = input().split(", ")
beggars = int(input())
result = []
for beg in range(beggars):
    new_num = 0
    try:
        get_nums = nums[::beggars]
        nums.remove(get_nums[0])
        for num in get_nums:
            new_num += int(num)
        result.append(new_num)
    except IndexError:
        result.append(new_num)
print(result)