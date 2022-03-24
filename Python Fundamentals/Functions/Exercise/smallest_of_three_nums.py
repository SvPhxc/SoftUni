def small_num(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(small_num(first_num, second_num, third_num))
