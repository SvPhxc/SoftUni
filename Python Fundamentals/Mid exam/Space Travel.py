rout = input().split("||")
fuel = int(input())
ammunition = int(input())
command = ""
int_num = 0

for i in rout:
    list1 = i.split(" ")
    command = list1[0]
    #print(command)
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    else:
        int_num = int(list1[1])
        #print(int_num)

    if command == "Travel":
        light_trip = fuel - int_num
        if light_trip > 0:
            print(f"The spaceship travelled {int_num} light-years.")
            fuel -= int_num
        else:
            print("Mission failed")
            break

    elif command == "Enemy":
        fight = ammunition - int_num
        if fight >= 0:
            print(f"An enemy with {int_num} armour is defeated.")
            ammunition -= int_num
        else:
            new_fight = fuel - (int_num * 2)
            if new_fight > 0:
                print(f"An enemy with {int_num} armour is outmaneuvered.")
                fuel -= 2 * int_num
            else:
                print("Mission failed.")
                break

    elif command == "Repair":
        fuel += int_num
        ammunition += 2 * int_num
        print(f"Ammunitions added: {2 * int_num}.")
        print(f"Fuel added: {int_num}.")

Chat Hello
Chat darling
Edit darling Darling
Spam how are you
Delete Darling
end

Chat John
Spam Let's go to the zoo
Edit zoo cinema
Chat tonight
Pin John
end