#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del(my_list[idx])
    return my_list

# It first checks if the provided index is out of range, and if
# so, it returns the original list without making any changes.
# If the index is valid, it uses the del statement to remove the
# item at the specified index and then return the modified list.
# It is important to note that the function modifies the original
# list, it will not return a new list with the specified element
# removed. This is important to consider if you want to keep the
# original list unchanged.
