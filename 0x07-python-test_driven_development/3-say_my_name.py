#!/usr/bin/python3
""" 3-say_my_name Module """


def say_my_name(first_name, last_name=""):
    """ Function that prints the input names """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name and last_name must be strings")
    print(f"My name is {first_name} {last_name}")
