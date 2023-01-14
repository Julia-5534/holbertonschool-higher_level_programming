#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for char_char in my_string:
        if char_char != 'c' and char_char != 'C':
            new_string += char_char
    return new_string
