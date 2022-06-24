def shopping_list(budget, **kwargs):
    bought = 0
    successfully_bought = []
    if budget < 100:
        return "You do not have enough budget."
    while True:
        for key in kwargs:
            total_price = kwargs[key][0] * kwargs[key][1]
            if bought >= 5:
                break
            if budget >= total_price:
                budget -= total_price
                result = f"You bought {key} for {total_price:.2f} leva."
                successfully_bought.append(result)
                bought += 1

                # print(result)
            elif budget < total_price:
                continue
        break


    return '\n'.join(successfully_bought)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
