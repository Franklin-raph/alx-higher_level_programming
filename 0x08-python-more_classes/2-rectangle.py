#!/usr/bin/python3
"""This module contains an empty Rectangle class"""


class Rectangle:
    """An empty rectangle class with no attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        wdt = self.__width
        hgt = self.__height
        if wdt == 0 or hgt == 0:
            return 0
        return (wdt + hgt) * 2
    
    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    @property
    def width(self):
        """Getter for the attribute __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the attribute __width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the attribute __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the attribute __height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value