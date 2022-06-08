#!/usr/bin/python3
def no_c(my_string):
    empty_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            empty_string += my_string[i]
    return empty_string
