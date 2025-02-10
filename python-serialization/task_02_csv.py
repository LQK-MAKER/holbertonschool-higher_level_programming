#!/usr/bin/python3
import csv
import json
"""
This module provides functions for serializing and deserializing."""


def convert_csv_to_json(csv_filename):
    """
    This function converts a CSV file to a JSON file.
    """

    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        with open(csv_filename.replace('.csv', '.json'), 'w') as json_file:
            json.dump(data, json_file, indent=4)

            return True
    except FileNotFoundError:
        return False
