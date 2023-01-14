#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))

# Uses tuple unpacking to unpack the values of a and b into
# a tuple, and then re-assigns the values of a and b to the
# unpacked values, swapping them.
