#!/usr/bin/python3
"""Module for Serializing json object"""
import json


def save_to_json_file(my_obj, filename):
    """Serializing json"""
    with open(filename, 'w', encoding='UTF-8') as outfile:
        json.dump(my_obj, outfile)
