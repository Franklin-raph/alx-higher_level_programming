#!/usr/bin/python3
"""Mod for file reading"""


def read_file(filename=""):
    """method for reading file"""
    with open(filename, 'r', encoding='UTF-8') as myfile:
        for line in myfile.readlines():
            print(line, end='')
