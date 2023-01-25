#!/usr/bin/python3
""" 4-print_square Module """


def print_square(size):
    """Function that prints squares using '#'"""
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
