file = open('./numbers.txt', 'r')
print(sum([int(x) for x in file]))