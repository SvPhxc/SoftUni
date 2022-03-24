def add_and_subtract(num1, num2, num3):
    def sum_numbers(num1, num2):
        sum_nums = num1 + num2
        return sum_nums
    def subtract(result, num3):
        final_result = result - num3
        return final_result
    return subtract(sum_numbers(num1, num2), num3)
first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
