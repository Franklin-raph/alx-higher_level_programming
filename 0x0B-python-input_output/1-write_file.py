#!/usr/bin/python3
"""Module for file writing"""


def write_file(filename="", text=""):
    """method for writing file"""
    num_of_chars = 0
    with open(filename, 'w', encoding='UTF-8') as myfile:
        num_of_chars = myfile.write(text)
    return num_of_chars
