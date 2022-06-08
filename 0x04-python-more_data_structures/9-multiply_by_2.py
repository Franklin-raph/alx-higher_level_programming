#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_values = a_dictionary.copy()
    new_ditionary = {}
    for i in dictionary_values:
        new_ditionary[i] = dictionary_values[i] * 2
    return new_ditionary

a_dictionary = {'John': 2, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
print(multiply_by_2(a_dictionary))