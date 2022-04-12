import re
count = int(input())
expression = r"^(\$|\%)(?P<name>[A-Z][a-z]+)\1\: (\[)(?P<num1>\d+)(\])(\|)\3(?P<num2>\d+)\5\6\3(?P<num3>\d+)\5\6$"
for x in range(count):
    text = input()
    match = re.match(expression, text)
    if match != None:
        tag = match.group("name")
        result = []
        num1 = match.group("num1")
        num2 = match.group("num2")
        num3 = match.group("num3")
        result.extend([chr(int(num1)), chr(int(num2)), chr(int(num3))])
        print(f"{tag}: {''.join(result)}")
    else:
        print("Valid message not found!")
