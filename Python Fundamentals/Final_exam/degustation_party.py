text = input().split("-")
guests = dict()
unliked_meals = 0
while ''.join(text) != "Stop":
    command = text[0]
    name = text[1]
    meal = text[2]
    if command == 'Like':
        if name not in guests.keys():
            guests[name] = list()
            guests[name].append(meal)
        else:
            pass
        if meal not in guests[name]:
            guests[name].append(meal)
        else:
            pass

    else:
        if name in guests.keys():
            if meal in guests[name]:
                guests[name].remove(meal)
                print(f"{name} doesn't like the {meal}.")
                unliked_meals += 1
            else:
                print(f"{name} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{name} is not at the party.")

    text = input().split("-")

for guest in guests:
    print(f"{guest}: {', '.join(guests[guest])}")
print(f"Unliked meals: {unliked_meals}")