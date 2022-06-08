#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_values = a_dictionary.copy()
    for i in dictionary_values:
        dictionary_values[i] = dictionary_values[i] * 2
    return dict(sorted(dictionary_values.items()))
