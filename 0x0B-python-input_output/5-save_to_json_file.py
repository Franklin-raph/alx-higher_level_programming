#!/usr/bin/python3
"""Module for returning a json string"""
import json


def save_to_json_file(my_obj, filename):
    """Serializing json"""
    json_object = json.dumps(my_obj, indent=1)
    with open(filename, 'w', encoding='UTF-8') as outfile:
        outfile.write(json_object)
