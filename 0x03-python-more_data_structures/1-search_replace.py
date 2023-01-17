#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list
    new_list = []
    # Iterate through each element in the original list
    for element in my_list:
        # If element = search element, add replacement element to new list
        if element == search:
            new_list.append(replace)
        # Otherwise, add the original element to the new list
        else:
            new_list.append(element)
    # Return the new list
    return new_list
