import re
text = input()
command = input().split(' ')
while ''.join(command) != "Done":
    if command[0] == "Change":
        if command[1] in text:
            text = text.replace(command[1], command[2])
            print(text)
        else:
            print(text)
    elif command[0] == "Includes":
        if command[1] in text:
            print(True)
        else:
            print(False)
    elif command[0] == "End":
        matches = re.finditer(r"\w+", text)
        output = []
        for match in matches:
            output.append(match)
        if command[1] == output[-1]:
            print(True)
        else:
            print(False)
    elif command[0] == "Uppercase":
        text = text.upper()
        print(text)
    elif command[0] == "FindIndex":
        print(text.find(command[1]))
    elif command[0] == "Cut":
        result = ''
        for x in range(int(command[2])):
            result += text[int(command[1]) + x]
        print(result)
    command = input().split(" ")