#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary
    new_dictionary = {}
    # Iterate through each key-value pair in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and add it to the new dictionary
        new_dictionary[key] = value * 2
    # Return the new dictionary
    return new_dictionary
