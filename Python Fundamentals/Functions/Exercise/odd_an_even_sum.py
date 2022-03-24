def odd_even(num):
    odd = 0
    even = 0
    for i in range(len(num)):
        num1 = int(num)
        digit = num1 // 10 ** i % 10
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
    print(f"Odd sum = {odd}, Even sum = {even}")


new_num = input()
odd_even(new_num)
