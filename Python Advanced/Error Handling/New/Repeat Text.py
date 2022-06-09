text = input()
try:
    num = int(input())
    for i in range(num):
        print(text, end='')
except ValueError:
    print("Variable times must be an integer")
