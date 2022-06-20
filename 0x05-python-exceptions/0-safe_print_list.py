#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ans = my_list[:x]
        for val in ans:
            print(val,end="")
    except:
        print("An error occured")