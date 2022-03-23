num = int(input())
for n in range(1, num + 1):
    sum_of_digits = 0
    digits = n
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    print(f"{n} -> {is_special}")
