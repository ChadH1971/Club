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


def to_string(a):
  my_list = []
  my_string = ""
  for i in a:
    b = 0
    c = 0
    k=int(math.log10(i))+1
    for j in range(k):
      b = ((i % 10)*(2**j))
      i = i // 10
      c = c + b
    my_list.append(c)
  for x in my_list:
    my_string = my_string + chr(x)
  return my_string


selection = input("Press 1 to convert from words to binary or 2 for binary to letters: ")
if selection == "1":
    user_input = input("Please enter the letters to convert: ")
    print(f"{user_input} in binary is ")
    print(to_binary(user_input))
elif selection == "2":
    n = int(input("Number of bytes to convert: "))
    user_input = list(map(int, input("Please enter each byte separated by a space: ").strip().split()))[:n]
    print(f"{user_input} in words is ")
    print(to_string(user_input))