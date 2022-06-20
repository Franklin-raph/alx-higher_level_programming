#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    ans = my_list[:x]
    for val in ans:
        try:
            print("{}".format(val), end="")
            counter += 1
        except IndexError:
            print("An error occured")
    print()
    return counter
