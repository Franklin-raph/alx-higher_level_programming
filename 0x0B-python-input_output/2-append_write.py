#!/usr/bin/python3
"""Module for file writing"""


def append_write(filename="", text=""):
    """method for appending to a file"""
    with open(filename, 'a') as fileHandle:
        fileHandle.write(text)
    fileHandle.close()

append_write("text1.txt", "hgfdsa")