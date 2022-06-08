#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    dictionary_values = a_dictionary.copy()
    for i in dictionary_values:
        new_dict[i] = dictionary_values[i] * 2
    return dict(sorted(new_dict.items()))
