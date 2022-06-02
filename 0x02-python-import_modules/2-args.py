#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if(len(argv) == 0):
        print(f"{len(argv)} arguements.")
    if(len(argv) == 1):
        print(f"{len(argv)} arguement.")
        for i in argv:
            print("{}: {}".format(argv.index(i) + 1, i))
    elif(len(argv) > 0):
        print(f"{len(argv)} arguements.")
        for i in argv:
            print("{}: {}".format(argv.index(i) + 1, i))
