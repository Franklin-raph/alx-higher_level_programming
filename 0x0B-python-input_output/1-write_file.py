#!/usr/bin/python3
"""Mod for file writing"""


def write_file(filename="", text=""):
    """method for writing file"""
    val = 0
    with open(filename, 'w', encoding='UTF-8') as myfile:
        val = myfile.write(text)
    return val
