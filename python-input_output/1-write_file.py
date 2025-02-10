#!/usr/bin/python3

"""Defines function."""


def write_file(filename="", text=""):
    """Write a string
    Args:
    filename (str):
    text (str):
    Returns:
    The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
