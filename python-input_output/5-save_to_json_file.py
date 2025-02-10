#!/usr/bin/python3

"""Defines function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
