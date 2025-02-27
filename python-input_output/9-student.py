#!/usr/bin/python3

"""class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str):
            last_name (str):
            age (int):
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
