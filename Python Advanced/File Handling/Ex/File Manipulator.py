from os import remove
from os.path import exists

while True:
    line = input()
    if line == "End":
        break
    command_parts = line.split('-')
    command, file_name = command_parts[0], command_parts[1]

    if command == 'Create':
        with open(f'./{file_name}', 'w') as file:
            pass
    elif command == 'Add':
        content = command_parts[2]
        with open(f'./{file_name}', 'w') as file:
            file.write(content + '\n')
    elif command == 'Replace':
        old_string, new_string = command_parts[2], command_parts[3]

        if not exists(f'./{file_name}'):
            print("An error occurred")
            continue
        with open(f'./{file_name}', 'a+') as file:
            file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(file_content)
    else:
        if not exists(f'./{file_name}'):
            print("An error occurred")
            continue
        remove(f'./{file_name}')


'''
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second
Line Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End

'''