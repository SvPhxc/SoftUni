commands = []
result = []
while "end" not in commands:

    new_commands = commands.append(input())

    command = ""
    for x in commands:
        list1 = x.split(" ")
        command = list1[0]
        list1.remove(list1[0])
        if command == "Chat":
            result.append(list1[0])
            commands.remove(x)
            break
        elif command == "Delete":
            if list1[0] in result:
                result.remove(list1[0])
                commands.remove(x)
                break
            else:
                break
        elif command == "Edit":
            if list1[0] in result:
                result.remove(list1[0])
                result.append(list1[1])
                commands.remove(x)
                break
            else:
                break
        elif command == "Pin":
            if list1[0] in result:
                result.remove(list1[0])
                result.append(list1[0])
                commands.remove(x)
                break
            else:
                break
        elif command == "Spam":
            for e in list1:
                result.append(e)
            commands.remove(x)
            break
for i in result:
    print(i)

