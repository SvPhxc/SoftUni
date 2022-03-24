def filter(nums):
    even_nums = []
    for num in nums:
        if int(num) % 2 == 0:
            even_nums.append(int(num))
    print(even_nums)


numbers = input().split(" ")
filter(numbers)
