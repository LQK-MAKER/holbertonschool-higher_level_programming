#!/usr/bin/python3
import json
"""
This module provides functions for serializing and deserializing."""


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)
        print(f"Data serialized and saved to '{filename}'.")


def load_and_deserialize(filename):
    """
    This function loads and deserializes data from a JSON file.
    """

    with open(filename, 'r') as file:
        data = json.load(file)
        return data
