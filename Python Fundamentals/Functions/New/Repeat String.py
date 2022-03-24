word = input()
counter = int(input())
def repeat(word, counter):
    for i in range(counter):
        print(word, end='')
repeat(word, counter)