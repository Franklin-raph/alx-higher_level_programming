#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

if(number < 0):
    print(f"Last digit of {number} is -{int(repr(number)[-1])} and is less than 6 and not 0")
elif(int(repr(number)[-1]) > 5):
    print(f"Last digit of {number} is {int(repr(number)[-1])} and is greater than 5")
elif(int(repr(number)[-1]) == 0):
    print(f"Last digit of {number} is {int(repr(number)[-1])} and is 0")
elif(int(repr(number)[-1]) < 6):
    print(f"Last digit of {number} is {int(repr(number)[-1])} and is less than 6 and not 0")
