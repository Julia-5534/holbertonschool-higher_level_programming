#!/usr/bin/python3

def print_integers(lst):
    for item in lst:
        if isinstance(item, int):
            print(item)

# This function takes in a list as an argument and iterates through each item in the list.
# For each item, it checks if the item is an instance of the int class using the isinstance()
# function. If it is, it prints the item.
