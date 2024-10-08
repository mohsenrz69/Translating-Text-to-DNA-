#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:29:09 2024

@author: mohsen
"""

# txt_to_DNA

# set variable with input text
original_str = input("What would you like to convert? ")
# convert text to binary values
binary_str = ''.join(format(x, '08b') for x in bytearray(original_str, 'utf-8'))

binary_list = [binary_str[i: i+2] for i in range(0, len(binary_str), 2)]

# binary values to nucleotide sequence
# remember:
# 00 = "A" (adenine)
# 01 = "G" (guanine)
# 10 = "C" (cytosine)
# 11 = "T" (thymine)

DNA_encoding = {
    "00": "A",
    "01": "G",
    "10": "C",
    "11": "T"
} 
DNA_list = []
for num in binary_list:
    for key in list(DNA_encoding.keys()):
        if num == key:
            DNA_list.append(DNA_encoding.get(key))

DNA_str = "".join(DNA_list)

# print input text, binary code and DNA sequence
print("\nThe original string is :" + "\n" + original_str + "\n")
print("The string after binary conversion is :" + "\n" + binary_str + "\n")
print("The string represented by single-letter codes is :" + "\n" + DNA_str + "\n")

