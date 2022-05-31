#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "and is less than 6 and not 0"
str2 = "and is greater than 5"
str3 = "and is less than 6 and not 0"
if(number < 0):
    print(f"Last digit of {number} is -{int(repr(number)[-1])} {str1}")
elif(int(repr(number)[-1]) > 5):
    print(f"Last digit of {number} is {int(repr(number)[-1])} {str2}")
elif(int(repr(number)[-1]) == 0):
    print(f"Last digit of {number} is {int(repr(number)[-1])} and is 0")
elif(int(repr(number)[-1]) < 6):
    print(f"Last digit of {number} is {int(repr(number)[-1])} {str3}")
