#!/usr/bin/python3
"""
print a text and new ligne with some character
character : . , ? and :
"""


def text_indentation(text):
    """
    the function
    """
    chara = [".", "?", ":"]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for t in range(len(text)):
        if text[t] in chara:
            print(text[t])
            print("")
        elif (text[t-1] in chara or text[t-1] == " ") and text[t] == " ":
            pass
        else:
            print(text[t], end="")
