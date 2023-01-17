#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()
    # Iterate through each element in the original list
    for element in my_list:
        # If the element is an integer and not already in the set, add to set
        if isinstance(element, int) and element not in unique_integers:
            unique_integers.add(element)
    # Return the sum of the unique integers
    return sum(unique_integers)
