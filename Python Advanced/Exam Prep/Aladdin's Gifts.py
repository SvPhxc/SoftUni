'''
105 20 30 25
120 60 11 400 10 1



'''


from collections import deque

materials = [int(x) for x in input().split(' ')]
magic_levels = deque([int(x) for x in input().split(' ')])


# def presents(sum_element):
#     if 100 <= sum_element <= 199:
#         return gemstone
#     elif 200 <= sum_element <= 299:
#         return porcelain_sculpture
#     elif 300 <= sum_element <= 399:
#         return gold
#     elif 400 <= sum_element <= 499:
#         return diamond_jewellery


gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()

    sum_elements = material + magic_level

    if sum_elements < 100:
        if sum_elements % 2 == 0:
            sum_elements = material * 2 + magic_level * 3
        else:
            sum_elements = material * 2 + magic_level * 2
    if sum_elements > 499:
        sum_elements /= 2

    gift = sum_elements // 100
    if gift == 1:
        gemstone += 1
    elif gift == 2:
        porcelain_sculpture += 1
    elif gift == 3:
        gold += 1
    elif gift == 4:
        diamond_jewellery += 1

if (gemstone and porcelain_sculpture) or (gold and diamond_jewellery):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

if gemstone:
    print(f"Gemstone: {gemstone}")

if porcelain_sculpture:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")

if gold:
    print(f"Gold: {gold}")

if diamond_jewellery:
    print(f"Diamond Jewellery: {diamond_jewellery}")


from collections import deque

materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])
presents = []

wedding_gifts = {
    1: "Gemstone",
    2: "Porcelain Sculpture",
    3: "Gold",
    4: "Diamond Jewellery"
}

while materials and magic_levels:
    material = materials.pop()
    level = magic_levels.popleft()
    mix = material + level

    if mix < 100:
        if mix % 2 == 0:
            mix = material * 2 + level * 3
        else:
            mix = material * 2 + level * 2

    if mix > 499:
        mix /= 2

    gift = wedding_gifts.get(mix // 100)
    if gift:
        presents.append(gift)

if wedding_gifts.get(1) in presents and wedding_gifts.get(2) in presents:
    print("The wedding presents are made!")
elif wedding_gifts.get(3) in presents and wedding_gifts.get(4) in presents:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left:', ', '.join([str(el) for el in materials]))
if magic_levels:
    print(f'Magic left:', ', '.join([str(el) for el in magic_levels]))

sorted_list = sorted([(el, presents.count(el)) for el in set(presents)])
for item in sorted_list:
    print(f'{item[0]}: {item[1]}')