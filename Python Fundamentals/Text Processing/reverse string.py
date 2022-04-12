text = input()
while text != 'end':
    reversed_word = ""
    for ch in reversed(text):
        reversed_word += ch
    print(f"{text} = {reversed_word}")

    text = input()


# helLo
# Softuni
# bottle
# end
