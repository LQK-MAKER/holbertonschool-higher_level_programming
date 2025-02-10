#!/usr/bin/python3

"""Defines function."""


def append_write(filename="", text=""):
    """Appends a string
    Args:
    filename (str):
    text (str):
    Returns:
    The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
