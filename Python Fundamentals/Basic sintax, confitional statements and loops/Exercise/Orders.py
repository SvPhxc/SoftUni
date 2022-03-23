orders = int(input())
total_price = 0
for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    order_sum = price_per_capsule * days * capsule_count
    total_price += order_sum
    print(f"The price for the coffee is: ${order_sum:.2f}")
print(f"Total: ${total_price:.2f}")
