#!/usr/bin/python3
"""This module provides functions for serializing and deserializing."""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """test"""

    root = ET.Element('data')
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
        root.append(element)
    tree = ET.ElementTree(root)
    
    with open(filename, 'wb') as file:
        tree.write(file)
        print(f"Data serialized and saved to '{filename}'.")

def deserialize_from_xml(filename):
    """test"""

    tree = ET.parse(filename)
    root = tree.getroot()
    datadict = {}
    for child in root:
        datadict[child.tag] = child.text
    return datadict
