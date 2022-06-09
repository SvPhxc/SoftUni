numbers_dictionary = {}
line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
        break
    line = input()

while line != "Remove":
    if numbers_dictionary == {}:
        break
    else:
        searched = input()
        try:
            print(numbers_dictionary[searched])
        except KeyError:
            print("Number does not exist in dictionary")
        line = input()
while line != "End":
    if numbers_dictionary == {}:
        break
    else:
        searched = input()
        try:
            numbers_dictionary.pop(searched)
        except KeyError:
            print("Number does not exist in dictionary")
        line = input()
print(numbers_dictionary)



'''
one
1
two
2
Search
one
Remove
two
End

one
two
Search
Remove
End

one
1
Search
one
Remove
two
End

'''