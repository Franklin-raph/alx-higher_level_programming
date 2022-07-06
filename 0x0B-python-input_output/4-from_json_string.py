#!/usr/bin/python3
"""Module for returning a json string"""
import json


def from_json_string(my_str):
    """method for returning a json string(deserializer)"""
    json.loads(my_str)
