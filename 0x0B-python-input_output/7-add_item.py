#!/usr/bin/python3

"""
Script: add_item_to_json_list

This script adds all command-line arguments to a Python
list and saves them to a JSON file.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Load existing items from the JSON file, if it exists
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(items, "add_item.json")

# Display the contents of the JSON file
try:
    items = load_from_json_file("add_item.json")
    print(items)
except FileNotFoundError:
    print("[]")
