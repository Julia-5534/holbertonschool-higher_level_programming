#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Use the built-in function 'sorted' to sort the keys
    for key in sorted(a_dictionary):
        print(key, ":", a_dictionary[key])
