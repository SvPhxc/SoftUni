order = input()
quantity = int(input())
def order_price(order, quantity):
    final_price = 0
    if order == 'coffee':
        final_price += quantity * 1.50
    elif order == 'water':
        final_price += quantity * 1.00
    elif order == 'coke':
        final_price += quantity * 1.40
    elif order == 'snacks':
        final_price += quantity * 2.00
    print(f"{final_price:.2f}")
order_price(order, quantity)