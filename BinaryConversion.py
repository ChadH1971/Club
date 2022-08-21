# www.educative.io
# CONTRIBUTOR

# Vivek Tangirala
# License: Creative Commons -Attribution -ShareAlike 4.0 (CC-BY-SA 4.0)
# with adaptations by Chad Hidalgo for clarity and selection of operation

import math


def to_binary(input_string):
    ascii_list, binary_list = [], []
    for index in input_string:
        ascii_list.append(ord(index))
    for index in ascii_list:
        binary_list.append(int(bin(index)[2:]))
    return binary_list


def to_string(input_chars):
    binary_list = []
    ascii_string = ""
    for i in input_chars:
        b = 0
        c = 0
        k = int(math.log10(i))+1
        for j in range(k):
            b = ((i % 10)*(2**j))
            i = i//10
            c = c+b
            binary_list.append(c)
            for x in binary_list:
                ascii_string = ascii_string + chr(x)
            return ascii_string


selection = input("Press 1 to convert from words to binary or 2 for binary to letters: ")
if selection == 1:
    user_input = input("Please enter the letters to convert: ")
    print(f"{user_input} in binary is ")
    print(to_binary(user_input))
elif selection == 2:
    user_input2 = input("Please enter the binary to convert: ")
    print(f"{user_input2} in words is ")
    print(to_string(user_input2))
