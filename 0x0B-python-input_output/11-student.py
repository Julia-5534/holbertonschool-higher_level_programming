#!/usr/bin/python3
"""11-student"""


class Student:
    """Defined by first name, last name, & age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
