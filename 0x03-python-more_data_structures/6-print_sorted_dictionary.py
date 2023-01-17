#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Use built-in function 'sorted' to sort the keys and iterate through them
    for key in sorted(a_dictionary.keys()):
        # Print the key and its corresponding value
        print(key, ":", a_dictionary[key])
