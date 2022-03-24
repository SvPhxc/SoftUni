operator = input()
num1 = int(input())
num2 = int(input())
def calculator(a, b, operator):
    result = 0
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    print(int(result))
calculator(num1, num2, operator)
