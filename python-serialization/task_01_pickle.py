#!/usr/bin/python3
import pickle
"""
This module provides functions for serializing and deserializing."""


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student


def display(self):
    print("Name: {self.name}")
    print("Age: {self.age}")
    print("Is student: {self.is_student}")


def serialize(self, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    except Exception as e:
        print("An error occurred: {e}")


@classmethod
def deserialize(cls, filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print("An error occurred: {e}")
        return None
