def char_in_range(char1, char2):
    char_n1 = ord(char1)
    char_n2 = ord(char2)
    for i in range(char_n1 + 1, char_n2):
        print(chr(i), end=' ')


first_char = input()
second_char = input()
char_in_range(first_char, second_char)
