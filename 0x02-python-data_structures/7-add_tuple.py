#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1+b1, a2+b2)

# This function takes two tuples as arguments. It uses if-else statements to
# check if the length of the tuple is greater than 0 and 1 and assigns values
# to a1, a2, b1, b2 respectively. If the tuple is smaller than 2, it uses the
# value 0 for each missing integer, if the tuple is bigger than 2, it uses only
# the first 2 integers. At the end it returns a tuple of 2 integers which are
# the addition of the first element of each argument and the addition of the
# second element of each argument. For example, if you call the function
# add_tuple((1,2),(3,4)), it will return (4,6).
