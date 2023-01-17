#!/usr/bin/python3
def best_score(a_dictionary):
    # check if dictionary is empty
    if not a_dictionary:
        return None
    # Use the built-in function 'max' to find the key with the highest value
    best_key = max(a_dictionary, key=a_dictionary.get)
    # Return the key with the highest value
    return best_key
