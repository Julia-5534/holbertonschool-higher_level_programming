#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use the built-in function to find the elements present in only one set
    return set_1.symmetric_difference(set_2)
