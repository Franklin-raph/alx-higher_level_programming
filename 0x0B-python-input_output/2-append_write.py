#!/usr/bin/python3
"""Module for file writing"""


def append_write(filename="", text=""):
    """method for appending to a file"""
    num_of_chars = 0
    with open(filename, 'a', encoding='UTF-8') as fileHandle:
        num_of_chars = fileHandle.write(text)
    fileHandle.close()
    return num_of_chars
